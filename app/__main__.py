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
# |--------------------------------------------------------------------------------------------------------------------|

import cv2
import numpy as np
import time
from resources.read_video import ReadVideo
from treatment.frame_modifications import rescale_frame
from infos.cv2_video_info import FPS

cap = ReadVideo("teste")
fps: FPS = FPS()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame: np.ndarray = rescale_frame(frame, 0.3)
    
    fps.get_fps()
    fps.putFPS(frame, "mean")
    fps.update_time()
    
    cv2.imshow("teste", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
    