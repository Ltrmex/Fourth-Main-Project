import argparse
import glob
import logging
import multiprocessing as mp
import os
import time

import cv2

from align import AlignDlib

logger = logging.getLogger(__name__)

align = AlignDlib(os.path.join(os.path.dirname(__file__), 'shape_predictor_68_face_landmarks.dat'))