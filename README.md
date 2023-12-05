# **Synthetic Tumors - Personal Modifications and Replication Work in Progress**

This forked repository encapsulates my personal modifications and ongoing replication endeavors based on the original repository available at https://github.com/MrGiovanni/SyntheticTumors. The primary focus of this replication effort lies in reproducing the findings detailed in the paper titled "[Label-Free Liver Tumor Segmentation](https://arxiv.org/pdf/2303.14869.pdf)." The provided data tables showcase my attempts at replicating the reported results and conducting additional experiments as part of this replication process. It's important to note that the information presented here reflects my individual efforts to validate and reproduce the referenced paper's methods, and may deviate to an extent from the original work. **Furthermore, the ultimate ownership of the current paper and code accomplishments resides with the original authors.** Updates and further details pertaining to this replication work will be continually added as the process unfolds.

## Default Evaluation

#### AI model trained by synthetic tumors(Downloaded,Control experiment)

|                       |  UNET (no.pretrain)  | Swin-UNETR-Base  (pretrain) | Swin-UNETR-Base (no.pretrain) | Swin-UNETR-Small (no.pretrain) | Swin-UNETR-Tiny (no.pretrain) |
| :-------------------: | :------------------: | :-------------------------: | :---------------------------: | :----------------------------: | :---------------------------: |
|      Liver Dice       |     **0.96093**      |         **0.96307**         |          **0.96441**          |          **0.96388**           |          **0.95996**          |
|       Liver Nsd       |     **0.87736**      |         **0.88440**         |          **0.89196**          |          **0.88591**           |          **0.87198**          |
|      Tumor Dice       | **0.57766** - 0.5981 |    **0.55722** - 0.5594     |     **0.53344** - 0.5594      |      **0.54794** - 0.5637      |     **0.52479** - 0.5510      |
|       Tumor Nsd       | **0.61974** - 0.6128 |    **0.60019** - 0.5820     |     **0.57556** - 0.5820      |      **0.57665** - 0.5824      |     **0.54078** - 0.5561      |
| Detection Sensitivity |          /           |          / - 0.832          |           / - 0.832           |           / - 0.814            |           / - 0.85            |

*/: No data available for this item.*

*-x: The item represents the original data in the paper.*

#### AI model trained by real tumors for comparison(Downloaded,Control experiment)

|                       |  UNET (no.pretrain)  |   Swin-UNETR-Base  (pretrain)    |  Swin-UNETR-Base (no.pretrain)  | Swin-UNETR-Small (no.pretrain) | Swin-UNETR-Tiny (no.pretrain) |
| :-------------------: | :------------------: | :------------------------------: | :-----------------------------: | :----------------------------: | :---------------------------: |
|      Liver Dice       |     **0.95290**      |           **0.96424**            |           **0.96737**           |          **0.96246**           |          **0.96115**          |
|       Liver Nsd       |     **0.85500**      |           **0.88934**            |           **0.90179**           |          **0.88162**           |          **0.87801**          |
|      Tumor Dice       | **0.53054** - 0.5763 | **0.55744** - 0.5902 - (0.5592)† | **0.59590** - 0.5902- (0.5592)† |      **0.55345** - 0.5849      |     **0.54777** - 0.5592      |
|       Tumor Nsd       | **0.55023** - 0.5810 |       **0.59046** - 0.6082       |      **0.61910** - 0.6082       |      **0.59696** - 0.5986      |     **0.56614** - 0.5655      |
| Detection Sensitivity |          /           |            / - 0.868             |            / - 0.868            |           / - 0.885            |           / - 0.858           |
#### AI model trained by synthetic tumors(Self)

|                       |  UNET (no.pretrain)  | Swin-UNETR-Base  (pretrain) | Swin-UNETR-Base (no.pretrain) | Swin-UNETR-Small (no.pretrain) | Swin-UNETR-Tiny (no.pretrain) |
| :-------------------: | :------------------: | :-------------------------: | :---------------------------: | :----------------------------: | :---------------------------: |
|         Epoch         |      4000(MAX)       |          4000(MAX)          |           4000(MAX)           |           4000(MAX)            |           4000(MAX)           |
|      Liver Dice       |     **0.96450**      |         **0.96476**         |          **0.96409**          |          **0.96401**           |          **0.96276**          |
|       Liver Nsd       |     **0.89170**      |         **0.89265**         |          **0.88995**          |          **0.88962**           |          **0.88353**          |
|      Tumor Dice       | **0.57500** - 0.5981 |    **0.57025** - 0.5594     |     **0.55158** - 0.5594      |      **0.54079** - 0.5637      |     **0.53372** - 0.5510      |
|       Tumor Nsd       | **0.62084** - 0.6128 |    **0.60829** - 0.5820     |      **0.60278** - 0.582      |      **0.58507** - 0.5824      |     **0.56287** - 0.5561      |
| Detection Sensitivity |          /           |          / - 0.832          |           / - 0.832           |           / - 0.814            |           / - 0.85            |

#### AI model trained by real tumors for comparison(Self)

|                       |  UNET (no.pretrain)  |   Swin-UNETR-Base  (pretrain)   | Swin-UNETR-Base (no.pretrain)  | Swin-UNETR-Small (no.pretrain) | Swin-UNETR-Tiny (no.pretrain) |
| :-------------------: | :------------------: | :-----------------------------: | :----------------------------: | :----------------------------: | :---------------------------: |
|         Epoch         |      4000(MAX)       |            4000(MAX)            |           4000(MAX)            |           4000(MAX)            |           4000(MAX)           |
|      Liver Dice       |     **0.95963**      |           **0.96585**           |          **0.96414**           |          **0.96415**           |          **0.96204**          |
|       Liver Nsd       |     **0.87500**      |           **0.89222**           |          **0.88773**           |          **0.88408**           |          **0.87628**          |
|      Tumor Dice       | **0.56542** - 0.5763 | **0.58100**- 0.5902 - (0.5592)† | **0.54147**- 0.5902- (0.5592)† |      **0.56391**- 0.5849       |      **0.53814**- 0.5592      |
|       Tumor Nsd       | **0.58887** - 0.5810 |       **0.61395**- 0.6082       |      **0.55647** - 0.6082      |      **0.59873**- 0.5986       |     **0.54783** - 0.5655      |
| Detection Sensitivity |          /           |            / - 0.868            |           / - 0.868            |           / - 0.885            |           / - 0.858           |

*†:The 5-fold cross validation results are provided by Tang et al.* 

#### Unet trained by mix tumors(4000 epochs, ≈ 1 : 1 CTs)

|   Metric   |   Fold 0    |   Fold 1    |   Fold 2    |   Fold 3    |   Fold 4    |         Ave          |
| :--------: | :---------: | :---------: | :---------: | :---------: | :---------: | :------------------: |
| Liver Dice | **0.95380** | **0.92759** | **0.95880** | **0.96200** | **0.95295** |     **0.95103**      |
| Liver Nsd  | **0.87248** | **0.81121** | **0.87985** | **0.87865** | **0.88415** |     **0.86527**      |
| Tumor Dice | **0.63622** | **0.52095** | **0.71753** | **0.54221** | **0.62109** | **0.60760** - 0.5686 |
| Tumor Nsd  | **0.66810** | **0.49405** | **0.75098** | **0.56155** | **0.64695** | **0.62433** - 0.5606 |

## Small Tumor Detection

|              | 0-5  | 5-10 | >10  |
| :----------: | :--: | :--: | :--: |
|    Truth     |  /   |  /   |  /   |
|   Real G.    |  /   |  /   |  /   |
| Synthetic G. |  /   |  /   |  /   |

## Ablation Study on Shape Generation(Unet)

| Tiny Size | Elastic Deformation | Edge Blurring | All Tumors DSC (%) | Small Tumors Det Sen. (%) |
| :-------: | :-----------------: | :-----------: | :----------------: | :-----------------------: |
|     √     |                     |               | **37.031** - 43.9  |         / - 26.4          |
|     √     |                     |       √       | **55.593*** - 47.1 |         / - 51.3          |
|     √     |          √          |               | **46.282** - 50.3  |         / - 54.1          |
|           |          √          |       √       | **53.796** - 52.6  |         / - 33.4          |
|     √     |          √          |       √       | **57.500** - 55.1  |         / - 61.8          |

**:The model has not gone through the full 4000 epochs of training.*