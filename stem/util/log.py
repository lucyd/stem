"""
Functions to aid library logging. Default logging is usually NOTICE and above,
runlevels being used as follows...

  ERROR  - critical issue occured, the user needs to be notified
  WARN   - non-critical issue occured that the user should be aware of
  NOTICE - information that is helpful to the user
  INFO   - high level library activity
  DEBUG  - low level library activity
  TRACE  - request/reply logging
"""

import logging

import stem.util.enum

# Logging runlevels. These are *very* commonly used so including shorter
# aliases (so they can be referenced as log.DEBUG, log.WARN, etc).

Runlevel = stem.util.enum.Enum(
  ("TRACE", "TRACE"),   ("DEBUG", "DEBUG"), ("INFO", "INFO"),
  ("NOTICE", "NOTICE"), ("WARN", "WARN"),   ("ERROR", "ERROR"))

TRACE, DEBUG, INFO, NOTICE, WARN, ERR = list(Runlevel)

# mapping of runlevels to the logger module's values, TRACE and DEBUG aren't
# built into the module

LOG_VALUES = {
  Runlevel.TRACE: logging.DEBUG - 5,
  Runlevel.DEBUG: logging.DEBUG,
  Runlevel.INFO: logging.INFO,
  Runlevel.NOTICE: logging.INFO + 5,
  Runlevel.WARN: logging.WARN,
  Runlevel.ERROR: logging.ERROR,
}

LOGGER = logging.getLogger("stem")

def get_logger():
  """
  Provides the stem logger.
  
  Returns:
    logging.Logger for stem
  """
  
  return LOGGER

def log(runlevel, message):
  """
  Logs a message at the given runlevel.
  
  Arguments:
    runlevel (Runlevel) - runlevel to log the message at, logging is skipped if
                          None
    message (str)       - message to be logged
  """
  
  if runlevel:
    LOGGER.log(LOG_VALUES[runlevel], message)

# shorter aliases for logging at a runlevel
def trace(message):  log(Runlevel.TRACE, message)
def debug(message):  log(Runlevel.DEBUG, message)
def info(message):   log(Runlevel.INFO, message)
def notice(message): log(Runlevel.NOTICE, message)
def warn(message):   log(Runlevel.WARN, message)
def error(message):  log(Runlevel.ERROR, message)
