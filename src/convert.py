# https://www.kaggle.com/datasets/motono0223/concrete-crack-segmentation-dataset

import os

from cv2 import connectedComponents
from tqdm import tqdm

import supervisely as sly
from supervisely.io.fs import get_file_name


def convert_and_upload_supervisely_project(api, workspace_id):
    project_name = "Concrete crack"
    dataset_path = "/private/tmp/sly_data_dir/concreteCrackSegmentationDataset"
    ds_name = "ds"
    batch_size = 3  # 4032x3024 images shapes...

    obj_class = sly.ObjClass("crack", sly.Bitmap, color=[208, 2, 27])
    obj_class_collection = sly.ObjClassCollection([obj_class])

    project_info = api.project.create(workspace_id, project_name)
    meta = sly.ProjectMeta(obj_classes=obj_class_collection)
    api.project.update_meta(project_info.id, meta.to_json())

    dataset = api.dataset.create(project_info.id, ds_name, change_name_if_conflict=True)

    images_pathes = os.path.join(dataset_path, "rgb")
    masks_pathes = os.path.join(dataset_path, "BW")
    images_names = os.listdir(images_pathes)

    def _create_ann(image_path):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        image_name = get_file_name(image_path)
        mask_path = os.path.join(masks_pathes, image_name + ".jpg")
        ann_np = sly.imaging.image.read(mask_path)[:, :, 2]
        mask = ann_np != 0
        ret, curr_mask = connectedComponents(mask.astype("uint8"), connectivity=8)
        for i in range(1, ret):
            obj_mask = curr_mask == i
            curr_bitmap = sly.Bitmap(obj_mask)
            if curr_bitmap.area > 100:
                curr_label = sly.Label(curr_bitmap, obj_class)
                labels.append(curr_label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

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
