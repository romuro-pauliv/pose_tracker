# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                        app/infos/cv2_video_info.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import numpy as np
import cv2
import time
# |--------------------------------------------------------------------------------------------------------------------|


class FPS(object):
    def __init__(self) -> None:
        """
        Initialize the FPS object with time, FPS values, and configurations for cv2.putText.

        Attributes:
            time_now (float): The current time when the object is created.
            R_FPS (float): The real-time frames per second.
            M_FPS (float): The mean frames per second.
            store_FPS (list[float]): A list to store recent FPS values.
            max_store (int): The maximum number of FPS values to store
        """
        self.time_now: float = time.time()
        
        self.R_FPS: float = 0
        self.M_FPS: float = 0
        
        self.store_FPS: list[float] = []
        self.max_store: int         = 30
        
        # cv2 PutText config
        self.coord      : tuple[int]    = (10, 10)
        self.font       : int           = 1
        self.font_scale : int           = 0.7
        self.color      : tuple[int]    = (0, 0, 0)
        self.thickness  : int           = 1
        self.line_type  : int           = 1
        
    def update_time(self) -> None:
        """
        Update the current time.
        """
        self.time_now: float = time.time()
    
    def _calc_m_fps(self) -> None:
        """
        Calculate the mean FPS and update the store_FPS list.

        If the length of store_FPS is less than max_store, append the current R_FPS to store_FPS.
        If the length of store_FPS equals max_store, remove the oldest FPS value and append the current R_FPS.
        """
        len_store: int = len(self.store_FPS)
        if len_store < self.max_store:
            self.store_FPS.append(self.R_FPS)
            return None
        if len_store == self.max_store:
            self.store_FPS: list[float] = self.store_FPS[1::]
            self.store_FPS.append(self.R_FPS)
            return None
    
    def get_fps(self) -> None:
        """
        Calculate the real-time FPS and update the mean FPS.

        The real-time FPS (R_FPS) is calculated as the reciprocal of the time difference
        between the current time and the last updated time.
        The mean FPS (M_FPS) is calculated as the average of the FPS values stored in store_FPS.
        """
        self.R_FPS: float = round(1/(time.time()-self.time_now), 2)
        self._calc_m_fps()
        self.M_FPS: float = round(sum(self.store_FPS)/len(self.store_FPS), 2)

    def putFPS(self, frame: np.ndarray, type_: str) -> None:
        """
        Draw the FPS value on a given frame using OpenCV's putText function.

        Args:
            frame (np.ndarray): The image/frame on which to draw the FPS value.
            type_ (str): The type of FPS to display ("mean" for M_FPS, otherwise R_FPS).

        The text is drawn at the position specified by self.coord, with the font, scale, color,
        thickness, and line type specified by the corresponding attributes.
        """
        cv2.putText(
            img         = frame,
            text        = f"M-FPS: {self.M_FPS}" if type_ == "mean" else f"R-FPS: {self.R_FPS}",
            org         = self.coord,
            fontFace    = self.font,
            fontScale   = self.font_scale,
            color       = self.color,
            thickness   = self.thickness,
            lineType    = self.line_type
        )