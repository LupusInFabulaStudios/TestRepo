from datetime import datetime
import time
import logzero
import os
from logzero import logger

logzero.logfile("/boot/logfile.log")

logger.info("Hello world!")
logger.info(f"Today is {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

logger.info("This should be found in the log. If it is, then it's working!")

logger.info("You can log all the information you want this way.")
logger.info("The path I set, as you can see, is the boot partition, so you can inspect it on windows and macos machines.")

logger.debug("Don't forget to shutdown your computer properly!")

os.system("shutdown now")
