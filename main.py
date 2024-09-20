from cvat_sdk.api_client import Configuration, ApiClient, models, apis, exceptions
from dotenv import load_dotenv
import os

load_dotenv()

configuration = Configuration(
    host="http://localhost",
    username=os.getenv("CVAT_USERNAME"),
    password=os.getenv("CVAT_PASSWORD"),
)

with ApiClient(configuration) as api_client:
    tasks_api = apis.TasksApi(api_client)
    tasks = tasks_api.list()
    print(tasks)