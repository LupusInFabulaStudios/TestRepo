from datetime import datetime
import time
import logzero
from logzero import logger

logzero.file("/tmp/logfile.log")

logger.info("Hello world!")
logger.info(f"Today is {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

logger.info("This should be found in the log. If it is, then it's working!")
