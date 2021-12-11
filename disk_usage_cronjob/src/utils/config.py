from dotenv import dotenv_values
import os

config = dotenv_values()  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
# print('[*] Config', config)
# print('[*] OS Config', os.getenv("INFLUXDB_CONTAINER_HOST"))
