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
    print(f"Starting download script")

