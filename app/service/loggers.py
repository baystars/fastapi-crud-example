# -*- mode: python -*- -*- coding: utf-8 -*-
import os
import logging
from logging.handlers import (RotatingFileHandler, SMTPHandler)

from app.config import LOG_DIR

def set_logger(logger, max_byte=100000, backup_count=10):
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    ## debug log
    debug_log = os.path.join(LOG_DIR, 'debug.log')
    debug_file_handler = RotatingFileHandler(debug_log, maxBytes=max_byte,
                                             backupCount=backup_count)
    debug_file_handler.setLevel(logging.INFO)
    debug_file_handler.setFormatter(formatter)
    logger.addHandler(debug_file_handler)
    ## error log (file handler)
    error_log = os.path.join(LOG_DIR, 'error.log')
    error_file_handler = RotatingFileHandler(error_log, maxBytes=max_byte,
                                             backupCount=backup_count)
    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(formatter)
    logger.addHandler(error_file_handler)
    ### error log (smtp handler)
    #error_smtp_handler = SMTPHandler(mailhost=app.config['SMTP_HOST'],
    #                                 fromaddr=app.config['SMTP_USER'],
    #                                 toaddrs=app.config['ADMINS'],
    #                                 subject='%s Failed'%app.config['APP_NAME'],
    #                                 credentials=(app.config['SMTP_USER'],
    #                                              app.config['SMTP_PASSWORD']))
    #error_smtp_handler.setLevel(logging.ERROR)
    #error_smtp_handler.setFormatter(formatter)
    #app.logger.addHandler(error_smtp_handler)
    # set default level
    logger.setLevel(logging.DEBUG)
