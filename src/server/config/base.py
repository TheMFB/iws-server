import os

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = False
WTF_CSRF_CHECK_DEFAULT = False

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "FufcDV5xeSEEEDxB5eIUcurb0HfCAThK3GquuDMO"

# Secret key for signing cookies
SECRET_KEY = "FufcDV5xeSEEEDxB5eIUcurb0HfCAThK3GquuDMO"

# Data and Response Statics
MAX_FEATURES = 50000
MAX_FEATURE_DATA_POINTS = 5000000
THROTTLE_TIME_LIMIT = 1  # seconds
MAX_APPLICATIONS = 1

# password hash
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = "LdEoN6wwNCEw9sh)qhjgZLExgrw4ZX8JDt9xZvY"

# security redirects
SECURITY_POST_LOGOUT_VIEW = '/login'
SECURITY_POST_LOGIN_VIEW = '/admin'
SECURITY_REGISTERABLE = False
SECURITY_RECOVERABLE = True

SECURITY_SEND_REGISTER_EMAIL = False

# ASF defaults
ASF_ADD_DEVICE_TIME = 3600 * 24
ASF_LEARNER_TRIGGER_RATE = 0.6
ASF_QUERY_OFFSET_SECONDS = 3600 * 24 * 6
ASF_DELTA_T = 120
ASF_AGGREGATION_TIMEOUT = 10 * 3600 * 24
ASF_LEARNER_TRIGGER_RATE = 0.6
ASF_QUERY_OFFSET_SECONDS = 3600 * 24 * 6
ASF_DELTA_T = 120
ASF_AGGREGATION_TIMEOUT = 10 * ASF_DELTA_T
ASF_CLUSTER_TIME = 86400
