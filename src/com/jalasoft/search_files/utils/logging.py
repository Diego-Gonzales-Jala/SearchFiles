#util/logging.py

import logging.config
from definition import CONFIG_PATH

logging.config.fileConfig(CONFIG_PATH)

logger = logging.getLogger('SearchFiles')


logger.warning("method_name::enter")

logger.warning("method_name::exit")