import logging
from logging.config import dictConfig
from pathlib import Path

import yaml

LOG = logging.getLogger(__name__)
LOGGING_CONFIG_PATH = Path(__file__).parent / "logging.yaml"


def setup_logging():
    with open(LOGGING_CONFIG_PATH) as f:
        log_config_dict = yaml.load(f, Loader=yaml.CSafeLoader)

    dictConfig(log_config_dict)

    LOG.info("Logging configured")
