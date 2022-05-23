# coding:utf-8

import logging
import os
import time

log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'

class Logger():
    def __init__(self):
        self.log_name = os.path.join(log_path, "%s.log" % time.strftime("%Y%m%d%H%M%S"))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter("%(asctime)s  %(filename)s"  "%(levelname)s"  "%(message)s")

        fh = logging.FileHandler(self.log_name)
        fh.setLevel(logging.INFO)
        fh.setFormatter(self.formatter)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(self.formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger
















