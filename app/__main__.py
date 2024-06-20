# Log Control |--------------------------------------------------------------------------------------------------------|
from log.genlog             import genlog
genlog.active_verbose()
genlog.active_color()
# |--------------------------------------------------------------------------------------------------------------------|

# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                    app/__main__.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import cv2
import numpy        as np

from resources.read_video           import ReadVideo
from treatment.frame_modifications  import rescale_frame, array2mediapipe_image
from infos.cv2_video_info           import FPS


from mediapipe.tasks.python.vision.pose_landmarker  import PoseLandmarker, PoseLandmarkerResult
from models.landmarker_options                      import LANDMAKER_OPTIONS
import mediapipe as mp
# |--------------------------------------------------------------------------------------------------------------------|

cap: cv2.VideoCapture = ReadVideo("teste")
fps: FPS = FPS()

with PoseLandmarker.create_from_options(LANDMAKER_OPTIONS) as landmarker:
    while cap.isOpened():
        # | Read frames |-------------------------------------------------------|
        ret, frame = cap.read()
        if not ret:
            break
        # |---------------------------------------------------------------------|
    
        # | frame treatment |---------------------------------------------------|
        frame   : np.ndarray    = rescale_frame(frame, 0.3)
        mp_frame: mp.Image      = array2mediapipe_image(frame)
        # |---------------------------------------------------------------------|

        # | MEDIAPIPE POSE TRACKER |--------------------------------------------|
        timestamp: float = cap.get(cv2.CAP_PROP_POS_MSEC)
        POSE_RESULT: PoseLandmarkerResult = landmarker.detect_for_video(
            image       = mp_frame,
            timestamp_ms= mp.Timestamp.from_seconds(timestamp).microseconds()
        )
        # |---------------------------------------------------------------------|
        
        
         
        # | FPS |---------------------------------------------------------------|
        fps.get_fps()
        fps.putFPS(frame, "mean")
        fps.update_time()
        # |---------------------------------------------------------------------|
    
        # | Show the frames |---------------------------------------------------|
        cv2.imshow("real video", frame)
        if cv2.waitKey(1) == ord("q"):
            break
        # |---------------------------------------------------------------------|
        
cap.release()
cv2.destroyAllWindows()
    