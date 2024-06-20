# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                   app/models/landmarker_options.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from mediapipe.tasks.python.vision.pose_landmarker  import PoseLandmarkerOptions
from mediapipe.tasks.python.core.base_options       import BaseOptions
from mediapipe.tasks.python.vision.pose_landmarker import _RunningMode
# |--------------------------------------------------------------------------------------------------------------------|

LANDMAKER_OPTIONS: PoseLandmarkerOptions = PoseLandmarkerOptions(
    base_options=BaseOptions(model_asset_path="app/models/pose_tracker/pose_landmarker_lite.task", delegate=1),
    running_mode=_RunningMode.VIDEO
)
