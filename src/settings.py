from typing import Dict, List, Optional, Union

from dataset_tools.templates import AnnotationType, CVTask, Industry, License

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME = "Concrete crack"
PROJECT_NAME_FULL = "Concrete crack Segmentation Dataset"

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_SA_4_0()
INDUSTRIES: List[Industry] = [Industry.Industrial()]
CV_TASKS: List[CVTask] = [CVTask.SemanticSegmentation(), CVTask.InstanceSegmentation()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.SemanticSegmentation()]

RELEASE_YEAR: int = 2022
HOMEPAGE_URL: str = "https://www.kaggle.com/datasets/motono0223/concrete-crack-segmentation-dataset"

PREVIEW_IMAGE_ID: int = 185895

GITHUB_URL: str = "https://github.com/dataset-ninja/concrete-crack-segmentation-"

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://www.kaggle.com/datasets/motono0223/concrete-crack-segmentation-dataset/download?datasetVersionNumber=1"

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = None
CITATION_URL: Optional[str] = None
ORGANIZATION_NAME: Optional[Union[str, List[str]]] = None
ORGANIZATION_URL: Optional[Union[str, List[str]]] = None
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME, PROJECT_NAME_FULL]
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL,
        "license": LICENSE,
        "industries": INDUSTRIES,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }
    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["tags"] = TAGS if TAGS is not None else []

    return settings
