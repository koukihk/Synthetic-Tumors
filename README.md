# **Synthetic Tumors - Personal Modifications and Replication Work in Progress**

This forked repository encapsulates my personal modifications and ongoing replication endeavors based on the original repository available at https://github.com/MrGiovanni/SyntheticTumors. The primary focus of this replication effort lies in reproducing the findings detailed in the paper titled "[Label-Free Liver Tumor Segmentation](https://arxiv.org/pdf/2303.14869.pdf)". The provided data tables showcase my attempts at replicating the reported results and conducting additional experiments as part of this replication process. It's important to note that the information presented here reflects my individual efforts to validate and reproduce the referenced paper's methods, and may deviate to an extent from the original work. **Furthermore,the ultimate ownership of the current paper and code accomplishments resides with the original author(s).** Updates and further details pertaining to this replication work will be continually added as the process unfolds.

## Default Evaluation

#### AI model trained by synthetic tumors(Downloaded,Control experiment)

|                       |  UNET (no.pretrain)  | Swin-UNETR-Base  (pretrain) | Swin-UNETR-Base (no.pretrain) | Swin-UNETR-Small (no.pretrain) | Swin-UNETR-Tiny (no.pretrain) |
| :-------------------: | :------------------: | :-------------------------: | :---------------------------: | :----------------------------: | :---------------------------: |
|      Liver Dice       |     **0.96093**      |         **0.96307**         |          **0.96441**          |          **0.96388**           |          **0.95996**          |
|       Liver Nsd       |     **0.87736**      |         **0.88440**         |          **0.89196**          |          **0.88591**           |          **0.87198**          |
|      Tumor Dice       | **0.57766** - 0.5981 |    **0.55722** - 0.5594     |     **0.53344** - 0.5594      |      **0.54794** - 0.5637      |     **0.52479** - 0.5510      |
|       Tumor Nsd       | **0.61974** - 0.6128 |    **0.60019** - 0.5820     |     **0.57556** - 0.5820      |      **0.57665** - 0.5824      |     **0.54078** - 0.5561      |

*/: No data available for this item.*

*-x: The item represents the original data in the paper.*

#### AI model trained by real tumors for comparison(Downloaded,Control experiment)

|                       |  UNET (no.pretrain)  |   Swin-UNETR-Base  (pretrain)    |  Swin-UNETR-Base (no.pretrain)  | Swin-UNETR-Small (no.pretrain) | Swin-UNETR-Tiny (no.pretrain) |
| :-------------------: | :------------------: | :------------------------------: | :-----------------------------: | :----------------------------: | :---------------------------: |
|      Liver Dice       |     **0.95290**      |           **0.96424**            |           **0.96737**           |          **0.96246**           |          **0.96115**          |
|       Liver Nsd       |     **0.85500**      |           **0.88934**            |           **0.90179**           |          **0.88162**           |          **0.87801**          |
|      Tumor Dice       | **0.53054** - 0.5763 | **0.55744** - 0.5902 - (0.5592)† | **0.59590** - 0.5902- (0.5592)† |      **0.55345** - 0.5849      |     **0.54777** - 0.5592      |
|       Tumor Nsd       | **0.55023** - 0.5810 |       **0.59046** - 0.6082       |      **0.61910** - 0.6082       |      **0.59696** - 0.5986      |     **0.56614** - 0.5655      |

#### AI model trained by synthetic tumors(Self)

|                       |  UNET (no.pretrain)  | Swin-UNETR-Base  (pretrain) | Swin-UNETR-Base (no.pretrain) | Swin-UNETR-Small (no.pretrain) | Swin-UNETR-Tiny (no.pretrain) |
| :-------------------: | :------------------: | :-------------------------: | :---------------------------: | :----------------------------: | :---------------------------: |
|         Epoch         |      4000(MAX)       |          4000(MAX)          |           4000(MAX)           |           4000(MAX)            |           4000(MAX)           |
|      Liver Dice       |     **0.96450**      |         **0.96476**         |          **0.96409**          |          **0.96401**           |          **0.96276**          |
|       Liver Nsd       |     **0.89170**      |         **0.89265**         |          **0.88995**          |          **0.88962**           |          **0.88353**          |
|      Tumor Dice       | **0.57500** - 0.5981 |    **0.57025** - 0.5594     |     **0.55158** - 0.5594      |      **0.54079** - 0.5637      |     **0.53372** - 0.5510      |
|       Tumor Nsd       | **0.62084** - 0.6128 |    **0.60829** - 0.5820     |      **0.60278** - 0.582      |      **0.58507** - 0.5824      |     **0.56287** - 0.5561      |

#### AI model trained by real tumors for comparison(Self)

|                       |  UNET (no.pretrain)  |   Swin-UNETR-Base  (pretrain)   | Swin-UNETR-Base (no.pretrain)  | Swin-UNETR-Small (no.pretrain) | Swin-UNETR-Tiny (no.pretrain) |
| :-------------------: | :------------------: | :-----------------------------: | :----------------------------: | :----------------------------: | :---------------------------: |
|         Epoch         |      4000(MAX)       |            4000(MAX)            |           4000(MAX)            |           4000(MAX)            |           4000(MAX)           |
|      Liver Dice       |     **0.95963**      |           **0.96585**           |          **0.96414**           |          **0.96415**           |          **0.96204**          |
|       Liver Nsd       |     **0.87500**      |           **0.89222**           |          **0.88773**           |          **0.88408**           |          **0.87628**          |
|      Tumor Dice       | **0.56542** - 0.5763 | **0.58100**- 0.5902 - (0.5592)† | **0.54147**- 0.5902- (0.5592)† |      **0.56391**- 0.5849       |      **0.53814**- 0.5592      |
|       Tumor Nsd       | **0.58887** - 0.5810 |       **0.61395**- 0.6082       |      **0.55647** - 0.6082      |      **0.59873**- 0.5986       |     **0.54783** - 0.5655      |

*†:The 5-fold cross validation results are provided by Tang et al.* 

#### Unet trained by mix tumors(4000 epochs, ≈ 1 : 1 CTs)

|   Metric   |   Fold 0    |   Fold 1    |   Fold 2    |   Fold 3    |   Fold 4    |         Ave          |
| :--------: | :---------: | :---------: | :---------: | :---------: | :---------: | :------------------: |
| Tumor Dice | **0.57777** | **0.56661** | **0.64459** | **0.57047** | **0.63288** | **0.59846** - 0.5686 |
| Tumor Nsd  | **0.58179** | **0.49007** | **0.67298** | **0.57742** | **0.65024** | **0.59450** - 0.5606 |

## Small Tumor Detection(Swin-UNETR)

|                |  0-5(Tiny)  | 5-10(Small) | 10-20(Medium) | >20(Large) |
| :------------: | :---------: | :---------: | :-----------: | :--------: |
|  Sample Num.   |     134     |     111     |      139      |     53     |
|   Real Sen.    | **0.4593** | **0.7870**  |  **0.7612**   | **0.6776** |
| Synthetic Sen. | **0.6734**  | **0.8815**  |  **0.9338**   | **0.9448** |
|    Ave Sen.    | **0.5663**  | **0.8342**  |  **0.8475**   | **0.8112** |

## Ablation Study on Shape Generation(Unet)

| Tiny Size | Elastic Deformation | Edge Blurring | All Tumors DSC (%) | Small Tumors Det Sen. (%) |
| :-------: | :-----------------: | :-----------: | :----------------: | :-----------------------: |
|     √     |                     |               | **37.031** - 43.9  |     **46.32** - 26.4      |
|     √     |                     |       √       | **55.593** - 47.1  |     **64.48** - 51.3      |
|     √     |          √          |               | **46.282** - 50.3  |     **38.32** - 54.1      |
|           |          √          |       √       | **53.796** - 52.6  |     **58.61** - 33.4      |
|     √     |          √          |       √       | **57.500** - 55.1  |     **67.86** - 61.8      |

**:The model has not gone through the full 4000 epochs of training.*
