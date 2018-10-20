# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

"""Factory method for easily getting imdbs by name."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__sets = {}
from datasets.pascal_voc import pascal_voc
from datasets.coco import coco
from datasets.imagenet import imagenet
from datasets.vg import vg

import numpy as np

import os.path

# Add devkit paths to your own folders. Add paths to folders containing VOCdevkit2007 in the format '$ROOT/dafrcnn-pytorch/data/src/$NAME_OF_YOUR_DATASET/VOCdevkit2007/'
# Add argument for domain.
"""
Dummy path:
for year in ['2007', '2012']:
  for split in ['train', 'val', 'trainval', 'test']:
    name = '$YOUR_DATASET_NAME_{}_{}'.format(year, split)
    file_src = '$ROOT/dafrcnn-pytorch/data/src/$YOUR_DATASET/VOCdevkit2007/' # Insert file path here
    assert os.path.exists(file_src), 'Invalid file path.'
    __sets[name] = (lambda split=split, year=year: pascal_voc(split, year, 'src', file_src ))
"""
###############################################################################

for year in ['2007', '2012']:
  for split in ['train', 'val', 'trainval', 'test']:
    name = 'city_{}_{}'.format(year, split)
    file_src = '/home/divyam/FRCN/dafrcnn-pytorch/data/src/cityscapes/VOCdevkit2007/' # Insert file path here
    assert os.path.exists(file_src), 'Invalid file path.'
    __sets[name] = (lambda split=split, year=year: pascal_voc(split, year, 'src', file_src ))

for year in ['2007', '2012']:
  for split in ['train', 'val', 'trainval', 'test']:
    name = 'fcity_{}_{}'.format(year, split)
    file_tar = '/home/divyam/FRCN/dafrcnn-pytorch/data/tar/foggy_cityscapes/VOCdevkit2007/' # Insert file path here
    assert os.path.exists(file_tar), 'Invalid file path.'
    __sets[name] = (lambda split=split, year=year: pascal_voc(split, year, 'tar', file_tar ))

###############################################################################
# Set up voc_<year>_<split>
for year in ['2007', '2012']:
  for split in ['train', 'val', 'trainval', 'test']:
    name = 'voc_{}_{}'.format(year, split)
    file_path = '/home/divyam/FRCN/dafrcnn-pytorch/data/VOC2007/VOCdevkit2007/' # Insert file path here
    assert os.path.exists(file_path), 'Invalid file path.'
    __sets[name] = (lambda split=split, year=year: pascal_voc(split, year, file_path ))

# Set up coco_2014_<split>
for year in ['2014']:
  for split in ['train', 'val', 'minival', 'valminusminival', 'trainval']:
    name = 'coco_{}_{}'.format(year, split)
    __sets[name] = (lambda split=split, year=year: coco(split, year))

# Set up coco_2014_cap_<split>
for year in ['2014']:
  for split in ['train', 'val', 'capval', 'valminuscapval', 'trainval']:
    name = 'coco_{}_{}'.format(year, split)
    __sets[name] = (lambda split=split, year=year: coco(split, year))

# Set up coco_2015_<split>
for year in ['2015']:
  for split in ['test', 'test-dev']:
    name = 'coco_{}_{}'.format(year, split)
    __sets[name] = (lambda split=split, year=year: coco(split, year))

# Set up vg_<split>
# for version in ['1600-400-20']:
#     for split in ['minitrain', 'train', 'minival', 'val', 'test']:
#         name = 'vg_{}_{}'.format(version,split)
#         __sets[name] = (lambda split=split, version=version: vg(version, split))
for version in ['150-50-20', '150-50-50', '500-150-80', '750-250-150', '1750-700-450', '1600-400-20']:
    for split in ['minitrain', 'smalltrain', 'train', 'minival', 'smallval', 'val', 'test']:
        name = 'vg_{}_{}'.format(version,split)
        __sets[name] = (lambda split=split, version=version: vg(version, split))

# set up image net.
for split in ['train', 'val', 'val1', 'val2', 'test']:
    name = 'imagenet_{}'.format(split)
    devkit_path = 'data/imagenet/ILSVRC/devkit'
    data_path = 'data/imagenet/ILSVRC'
    __sets[name] = (lambda split=split, devkit_path=devkit_path, data_path=data_path: imagenet(split,devkit_path,data_path))

def get_imdb(name):
  """Get an imdb (image database) by name."""
  if name not in __sets:
    raise KeyError('Unknown dataset: {}'.format(name))
  return __sets[name]()


def list_imdbs():
  """List all registered imdbs."""
  return list(__sets.keys())
