# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                              app/infos/cv2_pose.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import cv2
import numpy as np
from mediapipe.tasks.python.vision.pose_landmarker import PoseLandmarkerResult

from treatment.landmarker_result import frame_landmarker_coordinate
# |--------------------------------------------------------------------------------------------------------------------|


class PrintPose(object):
    def __init__(self, pose_result: PoseLandmarkerResult, frame: np.ndarray, pose: int) -> None:
        self.pose_result: PoseLandmarkerResult  = pose_result
        self.frame      : np.ndarray            = frame
        self.pose_num   : int                   = pose
        
        self.line_color : tuple[int] = (0, 255, 0)
        self.point_color: tuple[int] = (173, 255, 0)
    
        self.LEFT_HAND_CONN : list[tuple[int]] = [(18, 20), (20, 16), (18, 16), (22, 16)]
        self.LEFT_ARM_CONN  : list[tuple[int]] = [(16, 14), (14, 12)]
        self.RIGHT_HAND_CONN: list[tuple[int]] = [(19, 17), (19, 15), (15, 17), (21, 15)]
        self.RIGHT_ARM_CONN : list[tuple[int]] = [(15, 13), (11, 13)]
        self.TORSO_CONN     : list[tuple[int]] = [(12, 11), (11, 23), (12, 24), (24, 23)]
        self.LEFT_LEG_CONN  : list[tuple[int]] = [(24, 26), (26, 28)]
        self.LEFT_FOOT_CONN : list[tuple[int]] = [(28, 30), (30, 32), (28, 32)]
        self.RIGHT_LEG_CONN : list[tuple[int]] = [(23, 25), (25, 27)]
        self.RIGHT_FOOT_CONN: list[tuple[int]] = [(27, 29), (27, 31), (29, 31)]
        
        self.CONN_POINTS    : list[int] = list(range(11, 32))
        
        self.ALL_CONN: list[list[tuple[int]]] = [
            self.LEFT_HAND_CONN, self.LEFT_ARM_CONN,
            self.RIGHT_HAND_CONN, self.RIGHT_ARM_CONN,
            self.TORSO_CONN,
            self.LEFT_LEG_CONN, self.LEFT_FOOT_CONN,
            self.RIGHT_LEG_CONN, self.RIGHT_FOOT_CONN
            ]
        
    def _make_line(self, pts: tuple[tuple[int]]) -> None:
        cv2.line(
            img=self.frame,
            pt1=pts[0], pt2=pts[1],
            color=self.line_color,
            thickness=1
        )

    def _make_point(self, pt: tuple[int]) -> None:
        cv2.circle(
            img=self.frame,
            center=pt,
            radius=3,
            color=self.point_color,
            thickness=-1
        )
    
    def _make_head(self) -> None:
        indexes: list[int] = [0, 7, 8, 9, 10]
        
        for i in indexes:
            pt: tuple[int] = frame_landmarker_coordinate(self.frame, self.pose_result, self.pose_num, i)
            cv2.circle(
                img=self.frame,
                center=pt,
                radius=2,
                color=self.point_color,
                thickness=-1
            )
    
    def run(self) -> None:
        for members in self.ALL_CONN:
            for conn in members:
                pt1: tuple[int] = frame_landmarker_coordinate(self.frame, self.pose_result, self.pose_num, conn[0])
                pt2: tuple[int] = frame_landmarker_coordinate(self.frame, self.pose_result, self.pose_num, conn[1])
                self._make_line((pt1, pt2))
        
        for i in self.CONN_POINTS:
            pt: tuple[int] = frame_landmarker_coordinate(self.frame, self.pose_result, self.pose_num, i)
            self._make_point(pt)
        
        self._make_head()