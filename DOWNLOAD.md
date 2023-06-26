Dataset **Concrete Crack Segmentation** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/N/6/IM/C4MKxrRVPcYUp25FTja8In5HhUAIXz6yPgg8YsXGkhlKO6mve3Dpg9iuMXvzgOzFZd3Tf0HYU6ATGyHtyPTrwP7iPXVJqcC1CY65lY4okxCotE7WJJjXYHbhkZ0v.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Concrete Crack Segmentation', dst_path='~/dtools/datasets/Concrete Crack Segmentation.tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/motono0223/concrete-crack-segmentation-dataset/download?datasetVersionNumber=1)