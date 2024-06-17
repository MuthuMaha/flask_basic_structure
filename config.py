import os

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#SQLALCHEMY_DATABASE_URL = 'sqlite:///' + os.path.join(BASE_DIR,'app.db')
DATABASE_CONFIG = {
    'DRIVER' : 'ODBC Driver 17 for SQL Server',
    'SERVER' : 'localhost',
    'DATABASE' : 'tr8_test',
    'UID' : 'tr8_admin',
    'PWD' : 'Muthumaharajan@143',
}

SQLALCHEMY_DATABASE_URL = (
    f"mssql+pyodbc://@{DATABASE_CONFIG['SERVER']}/{DATABASE_CONFIG['DATABASE']}?trusted_connection=yes&driver={DATABASE_CONFIG['DRIVER'].replace(' ','+')}"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False