#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.
import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.33
        self.width = 0.50
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        # Define yourself dataset path
        self.data_dir = "cv_dataset_coco_v1"
        self.train_ann = "train.json"
        self.train_name = "train"
        self.val_ann = "val.json"
        self.val_name = "val"
        self.test_ann = "val.json"

        self.num_classes =6

        self.max_epoch = 30
        self.data_num_workers = 1
        self.eval_interval = 2
        self.basic_lr_per_img = 0.01 / 16.0
