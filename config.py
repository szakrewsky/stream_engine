import os
import sys
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

DBFILE_LOCATION = os.path.join(_basedir, 'preload.db')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DBFILE_LOCATION
DATABASE_CONNECT_OPTIONS = {}

CASSANDRA_CONTACT_POINTS = ['127.0.0.1']
CASSANDRA_KEYSPACE = 'ooi'
CASSANDRA_CONNECT_TIMEOUT = 10
CASSANDRA_FETCH_SIZE = 1000

SPREADSHEET_KEY = '1jIiBKpVRBMU5Hb1DJqyR16XCkiX-CuTsn1Z1VnlRV4I'
USE_CACHED_SPREADSHEET = False

#sys.path.append('ion-functions')
