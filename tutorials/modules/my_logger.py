import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--level", default=10, type=int)

allArgs = parser.parse_args()
logging.basicConfig(level=allArgs.level,
                    filename="some_logs.txt",
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug("\n")
logging.debug("This is a debug message: HELLO")
logging.info("This is a info message: HELLO")
logging.warning("This is a warning message: HELLO")
logging.error("This is a error message: HELLO")
logging.critical("This is a critical message: HELLO")