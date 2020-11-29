import logging

from rocohome.account import Account  # noqa: F401
from rocohome.building import Building  # noqa: F401
from rocohome.collector import Collector  # noqa: F401
from rocohome.device import Device  # noqa: F401
from rocohome.event import SensorEvent, decode_event  # noqa: F401
from rocohome.log_server import LogServer  # noqa: F401
from rocohome.sensor import Sensor  # noqa: F401
from rocohome.signal import Signal  # noqa: F401

logger = logging.getLogger(__name__)

fh = logging.FileHandler('rocohome.log')
fh.setLevel(logging.INFO)
logger.addHandler(fh)
