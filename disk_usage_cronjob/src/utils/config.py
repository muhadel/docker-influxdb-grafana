from dotenv import dotenv_values
import os

dotenv = dotenv_values()  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
config = {
    "INFLUXDB_URL": os.getenv("INFLUXDB_URL") or dotenv.get('INFLUXDB_URL'),
    "INFLUXDB_USERNAME": os.getenv("INFLUXDB_USERNAME") or dotenv.get('INFLUXDB_USERNAME'),
    "INFLUXDB_PASSWORD": os.getenv("INFLUXDB_PASSWORD") or dotenv.get('INFLUXDB_PASSWORD'),
    "INFLUXDB_ORG": os.getenv("INFLUXDB_ORG") or dotenv.get('INFLUXDB_ORG'),
    "INFLUXDB_BUCKET": os.getenv("INFLUXDB_BUCKET") or dotenv.get('INFLUXDB_BUCKET'),
    "INFLUXDB_ADMIN_TOKEN": os.getenv("INFLUXDB_ADMIN_TOKEN") or dotenv.get('INFLUXDB_ADMIN_TOKEN'),
    "INFLUXDB_CONTAINER_HOST": os.getenv("INFLUXDB_CONTAINER_HOST") or dotenv.get('INFLUXDB_CONTAINER_HOST'),
    "INFLUXDB_CONTAINER_PORT": os.getenv("INFLUXDB_CONTAINER_PORT") or dotenv.get('INFLUXDB_CONTAINER_PORT'),
    "INFLUXDB_CONTAINER_USER": os.getenv("INFLUXDB_CONTAINER_USER") or dotenv.get('INFLUXDB_CONTAINER_USER'),
    "INFLUXDB_CONTAINER_PASSWORD": os.getenv("INFLUXDB_CONTAINER_PASSWORD") or dotenv.get('INFLUXDB_CONTAINER_PASSWORD'),
}

