import logging
import logging.handlers
import re

class SensitiveDataFilter(logging.Filter):
     """Scrub passwords and tokens from log messages."""

     def filter(self, record):
          if isinstance(record.msg, str):
            record.msg = re.sub(r'password=\S+', 'password=*****', record.msg)
            record.msg = re.sub(r'token=\S+', 'token=****', record.msg)
          return True

app_logger = logging.getLogger('deploy_app')
app_logger.setLevel(logging.DEBUG)

db_logger = logging.getLogger('deploy_app.database')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

rot_file_handler = logging.handlers.RotatingFileHandler(
    'full_execution.log',
    maxBytes=2*1024,
    backupCount=5
)

rot_file_handler.setLevel(logging.DEBUG)

error_file_handler = logging.FileHandler('critical_errors.log')
error_file_handler.setLevel(logging.DEBUG)

standard_format = logging.Formatter('%(asctime)s | %(name)-18s | %(levelname)-8s | %(message)s')
detailed_format = logging.Formatter('%(asctime)s | %(name)-18s | %(levelname)-8s | [Func: %(funcName)s Line: %(lineno)d] | %(message)s')

console_handler.setFormatter(standard_format)
error_file_handler.setFormatter(standard_format)
rot_file_handler.setFormatter(detailed_format)


rot_file_handler.addFilter(SensitiveDataFilter())
error_file_handler.addFilter(SensitiveDataFilter())

app_logger.addHandler(console_handler)
app_logger.addHandler(rot_file_handler)
app_logger.addHandler(error_file_handler)

def run_deployment():
    app_logger.info("Strating deployment pipeline ...")
    app_logger.debug("Loaded configuration from /etc/config.yml")

    db_logger.info("Connecting to database.")
    db_logger.debug("Authenticating with db string: user=admin password=super_secret_db_pass token=abc123XYZ")

    try:
        1 / 0 
    except ZeroDivisionError:
        db_logger.error("Database schema migration failed!.")

    app_logger.critical("Deployment halted due to database failure.")

run_deployment()


