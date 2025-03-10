Dataset **Concrete Crack Segmentation** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzE4MzdfQ29uY3JldGUgQ3JhY2sgU2VnbWVudGF0aW9uL2NvbmNyZXRlLWNyYWNrLXNlZ21lbnRhdGlvbi1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICJQVXhiVE94YWdnUE5BOXp1NmRnMEQ0RnFZVFdBamxUMytmOCtrUHRsdzhvPSJ9)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Concrete Crack Segmentation', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/jwsn7tfbrp-1.zip).