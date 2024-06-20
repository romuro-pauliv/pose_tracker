# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                 app/treatment/landmarker_result.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from mediapipe.tasks.python.vision.pose_landmarker import PoseLandmarkerResult
import numpy as np
# |--------------------------------------------------------------------------------------------------------------------|


def frame_landmarker_coordinate(
    frame       : np.ndarray,
    pose_result : PoseLandmarkerResult,
    pose        : int,
    index       : int) -> tuple[np.float64]:
    x: float = pose_result.pose_landmarks[pose][index].x
    y: float = pose_result.pose_landmarks[pose][index].y
    
    return int(x*frame.shape[1]), int(y*frame.shape[0])
