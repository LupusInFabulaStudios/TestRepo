from datetime import datetime
import numpy as np
from logzero import logger

print("Hello world!")
print(f"Today is {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

x = np.array([[1,2,3],[4,5,6]])

logger.info(np.sqrt(x))
