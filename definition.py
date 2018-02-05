#here constants

import os

#read all loging.config, file definition where is logged
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATCH = os.patch.join(ROOT_DIR,'config\logging.conf')