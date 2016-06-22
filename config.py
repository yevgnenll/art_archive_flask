import os


# Statement for enabling the development environment
DEBUG = True

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL_DB')
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True
