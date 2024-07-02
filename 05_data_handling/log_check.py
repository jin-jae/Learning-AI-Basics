import logging

if __name__ == "__main__":
    logger = logging.getLogger("main")
    logging.basicConfig(level=logging.DEBUG)

    logger.debug("Test Log")
    logger.info("check")