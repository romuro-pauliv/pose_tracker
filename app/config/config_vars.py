# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                 analysis/app/config/config_vars.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from config.config_files import configfiles

from pathlib import Path, PosixPath
# |--------------------------------------------------------------------------------------------------------------------|


class ConfigPath(object):
    ROOT            : PosixPath = Path(configfiles.dot_ini['paths']['posixpath']['root'])
    EXTERNAL_DATA   : PosixPath = Path(configfiles.dot_ini['paths']['posixpath']['ext_data'])
    BIN_DATA        : PosixPath = Path(configfiles.dot_ini['paths']['posixpath']['ser_data'])
    VIDEOS_FILES    : PosixPath = Path(configfiles.dot_ini['paths']['posixpath']['videos_files'])
    MP_MODELS       : PosixPath = Path(configfiles.dot_ini['paths']['posixpath']['models'])

class FileExtensions(object):
    VIDEO       : str = str(configfiles.dot_ini['extensions']['ext']['video'])
    BIN         : str = str(configfiles.dot_ini['extensions']['ext']['bin'])
    MP_MODELS   : str = str(configfiles.dot_ini['extensions']['ext']['mp_models'])
    
class ConfigPoseLandmakerModel(object):
    MODEL_NAME  : str = str(configfiles.dot_ini['pose_landmarker']['base_options']['model_name'])
    DELEGATE    : str = str(configfiles.dot_ini['pose_landmarker']['base_options']['delegate'])