# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                               app/treatment/frame_modifications.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import cv2
import numpy        as np
import mediapipe    as mp
# |--------------------------------------------------------------------------------------------------------------------|

def rescale_frame(frame: np.ndarray, resize: int = 0.5) -> np.ndarray:
    """
    Rescale the frame
    Args:
        frame (np.ndarray): frame from OpenCV (cap.read())
        resize (int, optional): Values between [0, 1]. 1 to original scale. Defaults to 0.5.
    Returns:
        np.ndarray: Rescaled frame
    """
    width   : int   = int(frame.shape[1] * resize)
    height  : int   = int(frame.shape[0] * resize)
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_LINEAR)


def array2mediapipe_image(frame: np.ndarray) -> mp.Image:
    return mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)