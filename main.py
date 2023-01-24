from datetime import datetime
import time
import logzero
from logzero import logger

logzero.file("/boot/TestLogs/test.log")

logger.info("Hello world!")
logger.info(f"Today is {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

while True:
  logger.info("Boot2Repo is working! You may change the repository now.")
  time.sleep(5)
