import os

from dotenv import load_dotenv

load_dotenv()

RQUID = os.environ.get('RQUID')
AUTHORIZATION = os.environ.get('AUTHORIZATION')

