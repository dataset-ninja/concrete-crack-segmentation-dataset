# https://www.kaggle.com/datasets/motono0223/concrete-crack-segmentation-dataset

import os
from urllib.parse import unquote, urlparse

from cv2 import connectedComponents
from tqdm import tqdm
import numpy as np

import src.settings as s
import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import get_file_name


def download_dataset(teamfiles_dir: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
        parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name_with_ext = unquote(file_name_with_ext)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        local_path = os.path.join(storage_dir, file_name_with_ext)
        teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)
        api.file.download(team_id, teamfiles_path, local_path)

        dataset_path = unpack_if_archive(local_path)

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
        for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
            local_path = os.path.join(storage_dir, file_name_with_ext)
            teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

            if not os.path.exists(get_file_name(local_path)):
                api.file.download(team_id, teamfiles_path, local_path)

                sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
                unpack_if_archive(local_path)

            else:
                sly.logger.info(
                    f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
                )

        dataset_path = storage_dir
    return dataset_path


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    remote_dataset_path = "/4import/concreteCrackSegmentationDataset/"
    data_dir = sly.app.get_data_dir()
    dataset_path = os.path.join(data_dir, remote_dataset_path)
    if os.path.exists(dataset_path):
        sly.fs.clean_dir(dataset_path)
    api.file.download_directory(sly.env.team_id(), remote_dataset_path, dataset_path)
    ds_name = "ds"
    batch_size = 3  # 4032x3024 images shapes...

    obj_class = sly.ObjClass("crack", sly.Bitmap, color=[16, 138, 15])
    obj_class_collection = sly.ObjClassCollection([obj_class])

    project_info = api.project.create(workspace_id, project_name)
    meta = sly.ProjectMeta(obj_classes=obj_class_collection)
    api.project.update_meta(project_info.id, meta.to_json())

    dataset = api.dataset.create(project_info.id, ds_name)

    images_pathes = os.path.join(dataset_path, "rgb")
    masks_pathes = os.path.join(dataset_path, "BW")
    images_names = os.listdir(images_pathes)

    def _create_ann(image_path):

        image_name = get_file_name(image_path)
        mask_path = os.path.join(masks_pathes, image_name + ".jpg")
        ann_np = sly.imaging.image.read(mask_path)[:, :, 2]
        img_height = ann_np.shape[0]
        img_wight = ann_np.shape[1]
        mask = ann_np != 0
        bitmap = sly.Bitmap(mask)
        label = sly.Label(bitmap, obj_class)

        return sly.Annotation(img_size=(img_height, img_wight), labels=[label])


    progress = tqdm(desc=f"Create dataset {ds_name}", total=len(images_names))

    for img_names_batch in sly.batched(images_names, batch_size=batch_size):
        images_pathes_batch = [
            os.path.join(images_pathes, image_path) for image_path in img_names_batch
        ]

        anns_batch = [_create_ann(image_path) for image_path in images_pathes_batch]

        img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        api.annotation.upload_anns(img_ids, anns_batch)

        progress.update(len(img_names_batch))

    return project_info
