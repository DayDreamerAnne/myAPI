#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import logging.handlers
import sys
import os

import datetime

INFO = logging.INFO
DEBUG = logging.DEBUG
WARN = logging.WARN
ERROR = logging.ERROR
FATAL = logging.FATAL


def get_logger(level=INFO, also_to_stdout=False,):
    home = os.path.expanduser("~")
    log_dir = os.path.join(home, "logs")

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    script_name = 'EmployeeAPI'
    log_name = script_name + "_{}.log".format(datetime.date.today().strftime("%Y%m%d"))
    log_name = os.path.join(log_dir, log_name)

    logger = logging.getLogger(log_name)
    logger.setLevel(level)

    # check handler for this process already exists
    if len(logger.handlers) <= 0:
        # roll over at 5Mb, for at most of 2.5k times (12.5Gb) before last is file is overwritten
        handler = logging.handlers.RotatingFileHandler(log_name, 'a', 5242880, 2500, encoding='utf-8')

        formatter = logging.Formatter('%(asctime)s [%(levelname)s]\t%(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)

        if also_to_stdout:
            stdout_handler = logging.StreamHandler()
            stdout_handler.setFormatter(formatter)
            logger.addHandler(stdout_handler)

    return logger
