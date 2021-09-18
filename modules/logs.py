import logging

def createLog(message: str, nivel: int):
    log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'
    logging.basicConfig(filename='./log/osint.log',
                        filemode='w',
                        level=logging.DEBUG,
                        format=log_format)

    logger = logging.getLogger('root')

    if nivel == 0:
        logger.notset(message)
    elif nivel <= 10:
        logger.debug(message)
    elif nivel <= 20:
        logger.info(message)
    elif nivel <= 30:
        logger.warning(message)
    elif nivel <= 40:
        logger.error(message)
    elif nivel <= 50:
        logger.critical(message)