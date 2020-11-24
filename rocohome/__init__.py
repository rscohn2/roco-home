import logging

logger = logging.getLogger(__name__)

fh = logging.FileHandler('rocohome.log')
fh.setLevel(logging.INFO)
logger.addHandler(fh)
