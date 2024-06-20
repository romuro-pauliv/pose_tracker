# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                   app/models/landmarker_options.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from mediapipe.tasks.python.vision.pose_landmarker  import PoseLandmarkerOptions
from mediapipe.tasks.python.core.base_options       import BaseOptions
from mediapipe.tasks.python.vision.pose_landmarker import _RunningMode

from config.config_vars import ConfigPath, FileExtensions
from config.config_vars import ConfigPoseLandmakerModel as C

from pathlib import Path
# |--------------------------------------------------------------------------------------------------------------------|

LANDMAKER_OPTIONS_VIDEO: PoseLandmarkerOptions = PoseLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path=Path(ConfigPath.MP_MODELS, f"{C.MODEL_NAME}{FileExtensions.MP_MODELS}"),
        delegate=int(C.DELEGATE)
        ),
    running_mode=_RunningMode.VIDEO,
)