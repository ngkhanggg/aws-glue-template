import logging

formatter = logging.Formatter('%(levelname)s - %(asctime)s - %(filename)s:%(fileno)s: %(message)s')
logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
