from dotenv import dotenv_values
import os

dotenv = dotenv_values()  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
config = {
    "INFLUXDB_URL": os.getenv("INFLUXDB_URL") if  not dotenv.get('INFLUXDB_URL') else dotenv.get('INFLUXDB_URL'),
    "INFLUXDB_USERNAME": os.getenv("INFLUXDB_USERNAME") if  not dotenv.get('INFLUXDB_USERNAME') else dotenv.get('INFLUXDB_USERNAME'),
    "INFLUXDB_PASSWORD": os.getenv("INFLUXDB_PASSWORD") if  not dotenv.get('INFLUXDB_PASSWORD') else dotenv.get('INFLUXDB_PASSWORD'),
    "INFLUXDB_ORG": os.getenv("INFLUXDB_ORG") if  not dotenv.get('INFLUXDB_ORG') else dotenv.get('INFLUXDB_ORG'),
    "INFLUXDB_BUCKET": os.getenv("INFLUXDB_BUCKET") if  not dotenv.get('INFLUXDB_BUCKET') else dotenv.get('INFLUXDB_BUCKET'),
    "INFLUXDB_ADMIN_TOKEN": os.getenv("INFLUXDB_ADMIN_TOKEN") if  not dotenv.get('INFLUXDB_ADMIN_TOKEN') else dotenv.get('INFLUXDB_ADMIN_TOKEN'),
    "INFLUXDB_CONTAINER_HOST": os.getenv("INFLUXDB_CONTAINER_HOST") if  not dotenv.get('INFLUXDB_CONTAINER_HOST') else dotenv.get('INFLUXDB_CONTAINER_HOST'),
    "INFLUXDB_CONTAINER_PORT": os.getenv("INFLUXDB_CONTAINER_PORT") if  not dotenv.get('INFLUXDB_CONTAINER_PORT') else dotenv.get('INFLUXDB_CONTAINER_PORT'),
    "INFLUXDB_CONTAINER_USER": os.getenv("INFLUXDB_CONTAINER_USER") if  not dotenv.get('INFLUXDB_CONTAINER_USER') else dotenv.get('INFLUXDB_CONTAINER_USER'),
    "INFLUXDB_CONTAINER_PASSWORD": os.getenv("INFLUXDB_CONTAINER_PASSWORD") if  not dotenv.get('INFLUXDB_CONTAINER_PASSWORD') else dotenv.get('INFLUXDB_CONTAINER_PASSWORD'),

}
# print('[*] Config', config)
# print('[*] OS Config', os.getenv("INFLUXDB_CONTAINER_HOST"))
