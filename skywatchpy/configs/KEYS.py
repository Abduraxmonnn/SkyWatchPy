# Python
import os

# Foreign Libraries
from dotenv import load_dotenv

"""
This called for using .env and permission to read the variables from .env file
"""
load_dotenv()

"""
This variable is using for save the API_KEY for access to Weathers
"""
API_KEY = os.getenv('API_KEY')
API_URL = os.getenv('API_URL')
