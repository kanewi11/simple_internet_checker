from logging import getLogger, Formatter, WARNING
from logging.handlers import RotatingFileHandler
from time import sleep

from ping3 import ping, errors


SLEEP_TIME = 30  # Timeout
IPS = ['192.168.0.1', '8.8.8.8']  # Here you can add or remove ip by analogy

formatter = Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d.%m.%Y %H:%M:%S')

logger = getLogger(__name__)
logger.setLevel(WARNING)

file_handler = RotatingFileHandler('internet.log', maxBytes=10**6, backupCount=2, encoding='utf-8')
file_handler.setLevel(WARNING)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def ping_log(ip: str):
    try:
        if not ping(ip):
            logger.warning(f'{ip} | No response...')
    except errors.PingError as error:
        logger.warning(f'{ip} | {error}')


def main():
    while True:
        for ip in IPS:
            ping_log(ip)
        sleep(SLEEP_TIME)


if __name__ == '__main__':
    main()
