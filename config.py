import os
from dotenv import load_dotenv




load_dotenv(os.path.join(os.path.abspath(os.path.dirname(__file__)), '.env'))


class Config(object):
    SECRET_KEY = os.environ['SECRET_KEY']