import logging
logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename="main.log", level=logging.INFO)
    logger.info("Log started")

if __name__ == "__main__":
    main()
