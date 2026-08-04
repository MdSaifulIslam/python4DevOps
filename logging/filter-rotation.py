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

class OnlyInfoAndCriticalFilter(logging.Filter):
    def filter(self, record):
        return record.levelno in (logging.INFO, logging.CRITICAL)

class CustomConsoleAndFileHandler(logging.Handler):
    """
    A custom logging handler that prints logs in both Console and File.
    """
    def __init__(self, filename = "default_fixed.log"):
        super().__init__()
        self.filename = filename
        self.file_stream = open(self.filename, 'a', encoding='utf-8')

    def emit(self, record):
        try:
            # 1. Convert the LogRecord into a formatted string
            log_message = self.format(record)

            # --- Output A: The Console ---
            print(log_message)

            # --- Output B: The File ---
            self.file_stream.write(log_message + '\n')
            self.file_stream.flush()
            
        except Exception:
            # Built-in logging fallback in case formatting or printing fails
            self.handleError(record)

    def close(self):
        if hasattr(self, 'file_stream') and not self.file_stream.closed:
            self.file_stream.close()
        super().close()

app_logger = logging.getLogger('deploy_app')
app_logger.setLevel(logging.INFO)

db_logger = logging.getLogger('deploy_app.database')
db_logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

rot_file_handler = logging.handlers.RotatingFileHandler(
    'full_execution.log',
    maxBytes=2*1024,
    backupCount=3,
    encoding="utf-8"
)

rot_file_handler.setLevel(logging.DEBUG)

error_file_handler = logging.FileHandler('critical_errors.log')
error_file_handler.setLevel(logging.DEBUG)

standard_format = logging.Formatter('%(asctime)s | %(name)-18s | %(levelname)-8s | %(message)s')
custom_format = logging.Formatter('%(asctime)s | %(name)-18s | %(levelname)-8s | %(message)s -From custom dual Handler')
detailed_format = logging.Formatter('%(asctime)s | %(name)-18s | %(levelname)-8s | [Func: %(funcName)s Line: %(lineno)d] | %(message)s')

console_handler.setFormatter(standard_format)
error_file_handler.setFormatter(standard_format)
error_file_handler.addFilter(OnlyInfoAndCriticalFilter())
rot_file_handler.setFormatter(detailed_format)


rot_file_handler.addFilter(SensitiveDataFilter())
error_file_handler.addFilter(SensitiveDataFilter())

custom_handler = CustomConsoleAndFileHandler("extra.log")
custom_handler.setFormatter(custom_format)
custom_handler.setLevel(logging.DEBUG)


app_logger.addHandler(console_handler)
app_logger.addHandler(rot_file_handler)
app_logger.addHandler(error_file_handler)
app_logger.addHandler(custom_handler)

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


