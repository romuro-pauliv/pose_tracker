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

class FileExtensions(object):
    VIDEO: str = str(configfiles.dot_ini['extensions']['ext']['video'])
    BIN  : str = str(configfiles.dot_ini['extensions']['ext']['bin'])