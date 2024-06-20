# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                        app/resources/read_video.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from config.config_vars     import ConfigPath, FileExtensions
from log.genlog             import genlog

from pathlib                import Path, PosixPath

import cv2
# |--------------------------------------------------------------------------------------------------------------------|


def ReadVideo(filename: str) -> cv2.VideoCapture:
    """
    Read video with OpenCV
    Args:
        filename (str): The video filename (without extension)
    Returns:
        cv2.VideoCapture: The video in OpenCV Object
    """
    path_: PosixPath = Path(ConfigPath.VIDEOS_FILES, f"{filename}{FileExtensions.VIDEO}")
    genlog.log(True, path_, False)
    return cv2.VideoCapture(path_)