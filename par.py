import sys
import os
import re
import subprocess
import tempfile
from PIL import Image


def parse_captcha(filename):
    """Return the text for thie image using Tesseract
    """
    img = threshold(filename)
    return tesseract(img)
