Dataset **Concrete crack** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/h/U/WQ/gAtkOvnGUCKdYO24WSUeQGuevZEkH9q8eWegwZcnCR9ZoDglHtcrTb0jLONttZfP1Cb5xouFzLQXIgV0vP2UuuxHstk2BhithxvrAcBXxyfTJVoPNgPiNlot6Zz5.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Concrete crack', dst_path='~/dtools/datasets/Concrete crack.tar')
```
The data in original format can be 🔗[downloaded here.](https://www.kaggle.com/datasets/motono0223/concrete-crack-segmentation-dataset/download?datasetVersionNumber=1)