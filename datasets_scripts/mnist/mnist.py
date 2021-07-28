from __future__ import (absolute_import, division, print_function, unicode_literals)
import yaml
import os
import logging
import logging.config
import argparse
from enum import Enum
from typing import List
import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import get_file

def download():

    if args.dataDir is None:
        raise ValueError("Data directory is not specified (did you use --data-dir=PATH?)")
    os.makedirs(args.dataDir, exist_ok=True)

    data_file = os.path.join(args.dataDir, 'mnist.npz')
    if os.path.exists(data_file):
        print("MNIST data has already been download (file exists: %s)", data_file)
        return

    data_file = get_file(
        fname=data_file,
        origin='https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz',
        file_hash='731c5ac602752760c8e48fbffcf8c3b850d9dc2a2aedcf2cc48468fc17b673d1'
    )

    if not os.path.isfile(data_file):
        raise ValueError(f"MNIST dataset has not been downloaded - dataset file does not exist: {data_file}")
    else:
        print("MNIST dataset has been downloaded.")
    print("The downlaod task has been completed.")


if __name__=="__main__":
    download()
