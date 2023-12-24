import random
from typing import Hashable, Mapping, Dict

from monai.config import KeysCollection
from monai.config.type_definitions import NdarrayOrTensor
from monai.transforms.transform import MapTransform, RandomizableTransform

from .utils import SynthesisTumor, get_predefined_texture
import numpy as np

import os
import nibabel as nb
import glob

class TumorGenerated(RandomizableTransform, MapTransform):
    def __init__(self, 
    keys: KeysCollection, 
    prob: float = 0.1,
    tumor_prob = [0.2, 0.2, 0.2, 0.2, 0.2],
    allow_missing_keys: bool = False
    ) -> None:
        MapTransform.__init__(self, keys, allow_missing_keys)
        RandomizableTransform.__init__(self, prob)
        random.seed(0)
        np.random.seed(0)

        self.tumor_types = ['tiny', 'small', 'medium', 'large', 'mix']
        
        assert len(tumor_prob) == 5
        self.tumor_prob = np.array(tumor_prob)
        # texture shape: 420, 300, 320
        # self.textures = pre_define 10 texture
        self.textures = []
        sigma_as = [3, 6, 9, 12, 15]
        sigma_bs = [4, 7]
        predefined_texture_shape = (420, 300, 320)
        for sigma_a in sigma_as:
            for sigma_b in sigma_bs:
                texture = get_predefined_texture(predefined_texture_shape, sigma_a, sigma_b)
                self.textures.append(texture)
        print("All predefined texture have generated.")

    def save_synthetic_data(self, d, tumor_type):
        volume_scan = d['image'][0]
        mask_scan = d['label'][0]

        image_affine = d["image_meta_dict"]["affine"]
        label_affine = d["label_meta_dict"]["affine"]

        image_spatial_shape = d["image_meta_dict"]["spatial_shape"]
        label_spatial_shape = d["label_meta_dict"]["spatial_shape"]

        # Save the images
        root_dir = 'datafolds'
        output_dir = os.path.join(root_dir, 'synt_af', tumor_type)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        output_img_dir = os.path.join(output_dir, 'img')
        if not os.path.exists(output_img_dir):
            os.makedirs(output_img_dir)

        output_label_dir = os.path.join(output_dir, 'label')
        if not os.path.exists(output_label_dir):
            os.makedirs(output_label_dir)

        existing_files = glob.glob(os.path.join(output_img_dir, '*.nii.gz'))
        counter = len(existing_files)

        nb.save(
            nb.Nifti1Image(volume_scan.astype(np.float32), image_affine),
            os.path.join(output_img_dir, f'{counter}.nii.gz')
        )

        nb.save(
            nb.Nifti1Image(mask_scan.astype(np.uint8), label_affine),
            os.path.join(output_label_dir, f'{counter}.nii.gz')
        )

    def __call__(self, data: Mapping[Hashable, NdarrayOrTensor]) -> Dict[Hashable, NdarrayOrTensor]:
        d = dict(data)
        self.randomize(None)

        if self._do_transform and (np.max(d['label']) <= 1):  
            tumor_type = np.random.choice(self.tumor_types, p=self.tumor_prob.ravel())
            texture = random.choice(self.textures)
            d['image'][0], d['label'][0] = SynthesisTumor(d['image'][0], d['label'][0], tumor_type, texture)
            # print(tumor_type, d['image'].shape, np.max(d['label']))
            # print("Image meta dict:", d["image_meta_dict"])
            # print("Label meta dict:", d["label_meta_dict"])
            # self.save_synthetic_data(d, tumor_type)

        return d
