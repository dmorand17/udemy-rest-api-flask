import os.path
import sys


class AppUtils:
    @staticmethod
    def path_exists(path):
        if not os.path.exists(path):
            return False
        return True
