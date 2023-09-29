import argparse
import os

import cv2
import mmcv
import torch
import numpy as np
import json

from mmcv.parallel import MMDataParallel, MMDistributedDataParallel
from mmcv.runner import get_dist_info, init_dist, load_checkpoint
from tools.fuse_conv_bn import fuse_module

from mmdet.apis import multi_gpu_test, single_gpu_test
from mmdet.core import wrap_fp16_model
from mmdet.datasets import build_dataloader, build_dataset
from mmdet.datasets.cityscapes import PALETTE
from mmdet.models import build_detector
from mmdet.apis import init_detector, inference_detector, show_result
from mmdet.core import cityscapes_originalIds

from PIL import Image
from skimage.morphology import dilation
from skimage.segmentation import find_boundaries
from cv2.typing import MatLike


def execute_efficientps(img: MatLike):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = current_dir + '/kitti_config.py'
    checkpoint_file = current_dir + '/model_kt.pth'

    device = torch.device('cuda:0')
    cfg = mmcv.Config.fromfile(config_file)

    model = init_detector(config_file, checkpoint_file, device=device)

    PALETTE.append([0,0,0])
    colors = np.array(PALETTE, dtype=np.uint8)

    img_shape = img.shape[:2][::-1]
    img_ = cv2.resize(img, cfg.test_pipeline[1]['img_scale'])

    result = inference_detector(model, img_, eval='panoptic')
    pan_pred, _, _ = result[0]

    panoptic_col = pan_pred
    pan_pred = pan_pred.numpy()
    panoptic_col[pan_pred==0] = colors.shape[0] - 1
    panoptic_col = Image.fromarray(colors[panoptic_col])

    out = panoptic_col.convert(mode="RGB")

    return cv2.resize(np.array(out)[:,:,::-1], img_shape)
