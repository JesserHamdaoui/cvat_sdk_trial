from cvat_sdk import Configuration, ApiClient, models, apis, exceptions
from dotenv import load_dotenv
import os

load_dotenv()

configuration = Configuration(
    host="http://localhost",
    username= os.getenv('CVAT_USERNAME'),
    password=os.getenv('CVAT_PASSWORD')
)

