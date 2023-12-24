# Installation

#### Dataset

please download these datasets and save to `<data-path>` (user-defined).

- 01 [Multi-Atlas Labeling Beyond the Cranial Vault - Workshop and Challenge (BTCV)](https://www.synapse.org/#!Synapse:syn3193805/wiki/89480)
- 02 [Pancreas-CT TCIA](https://wiki.cancerimagingarchive.net/display/Public/Pancreas-CT)
- 03 [Combined Healthy Abdominal Organ Segmentation (CHAOS)](https://chaos.grand-challenge.org/)
- 04 [Liver Tumor Segmentation Challenge (LiTS)](https://competitions.codalab.org/competitions/17094)

```bash
wget https://www.dropbox.com/s/jnv74utwh99ikus/01_Multi-Atlas_Labeling.tar.gz # 01 Multi-Atlas_Labeling.tar.gz (1.53 GB)
wget https://www.dropbox.com/s/5yzdzb7el9r3o9i/02_TCIA_Pancreas-CT.tar.gz # 02 TCIA_Pancreas-CT.tar.gz (7.51 GB)
wget https://www.dropbox.com/s/lzrhirei2t2vuwg/03_CHAOS.tar.gz # 03 CHAOS.tar.gz (925.3 MB)
wget https://www.dropbox.com/s/2i19kuw7qewzo6q/04_LiTS.tar.gz # 04 LiTS.tar.gz (17.42 GB)
```

#### Dependency
The code is tested on `python 3.8, Pytorch 1.11`.
```bash
conda create -n syn python=3.8
source activate syn (or conda activate syn)
cd SyntheticTumors
pip install external/surface-distance
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
pip install -r requirements.txt
```

#### Label

Our synthetic algorithm requires label as ``0: background, 1: liver``, you need to transfer the label before training AI model.

```bash 
python transfer_label.py --data_path <data-path>  # <data-path> is user-defined data path to save datasets
```
or you can just download the label
```
wget https://www.dropbox.com/s/8e3hlza16vor05s/label.zip
```
