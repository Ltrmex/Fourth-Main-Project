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

def preprocessImage(inputPath, outputPath, cropDim):
    """
    Detect face, align and crop :param inputPath. Write output to :param outputPath
    :param inputPath: Path to input image
    :param outputPath: Path to write processed image
    :param cropDim: dimensions to crop image to
    """
    image = _process_image(inputPath, cropDim)
    if image is not None:
        logger.debug('Writing processed file: {}'.format(outputPath))
        cv2.imwrite(outputPath, image)
    else:
        logger.warning("Skipping filename: {}".format(inputPath))

def _processImage(filename, cropDim):
    image = None
    alignedImage = None

    image = _bufferImage(filename)

    if image is not None:
        alignedImage = _alignImage(image, cropDim)
    else:
        raise IOError('Error buffering image: {}'.format(filename))

    return alignedImage