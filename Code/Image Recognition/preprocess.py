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

def main(inputDir, outputDir, cropDim):
    startTime = time.time()
    pool = mp.Pool(processes)

    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    for image_dir in os.listdir(inputDir):
        imageOutput = os.path.join(outputDir, os.path.basename(os.path.basename(image_dir)))
        if not os.path.exists(imageOutput):
            os.makedirs(imageOutput)

    imagePaths = glob.glob(os.path.join(inputDir, '**/*.jpg'))
    for index, imagePath in enumerate(imagePaths):
        imageOutput = os.path.join(outputDir, os.path.basename(os.path.dirname(imagePath)))
        outputPath = os.path.join(imageOutput, os.path.basename(imagePath))
        pool.apply_async(preprocess_image, (imagePath, outputPath, cropDim))

    pool.close()
    pool.join()
    logger.info('Completed in {} seconds'.format(time.time() - startTime))

