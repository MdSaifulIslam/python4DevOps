# Log levels in practice

# Two-stage filtering

# Configuring logs and handlers


import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('automation_debug.log')
file_handler.setLevel(logging.DEBUG)

console_format = logging.Formatter('%(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [Line: %(lineno)d] - %(message)s')

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("Conecting to AWS API ... [Token: 12345]")
logger.info("Deployment script started.")
logger.warning("Config file missing, using defaults.")
logger.error("Failed to restart the service.")