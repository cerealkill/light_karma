# -*- coding: utf-8 -*-


class Loader:
    """
    General class for objects that read data from Excel, PDF, CSV, Word and any other unstructured data sources and 
     parse it into an structured data object that is saved to disk in a python pickle file.
    :arg file_path: String containing file path to load
    :arg pkl_file: String with Pickle file path to store object in disk
    :param loaded_object: Object created by loading the designed file.
    """
    def __init__(self, file_path, pkl_file):
        self._file_path = file_path
        self._pkl_file = pkl_file
        self._loaded_object = None

    def _read(self):
        pass

    @property
    def loaded_object(self):
        return self._loaded_object
