from cvat_sdk import Config, Client, models
from cvat_sdk.core.proxies.tasks import ResourceType, Task
from dotenv import load_dotenv
import os

load_dotenv()
config = Config()

# print(os.getenv("CVAT_USERNAME"))
# print(os.getenv("CVAT_PASSWORD"))

with Client("https://localhost", config=config) as client:
    client.login((os.getenv("CVAT_USERNAME"), os.getenv("CVAT_PASSWORD")))
    print(client)
