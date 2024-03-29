from influxdb import InfluxDBClient
from utils.config import config


class InfluxDB:
    __influx_client = None
    host = config.get('INFLUXDB_CONTAINER_HOST').strip()
    port = config.get('INFLUXDB_CONTAINER_PORT').strip()
    username = config.get('INFLUXDB_USERNAME').strip()
    password = config.get('INFLUXDB_PASSWORD').strip()
    bucket = config.get('INFLUXDB_BUCKET').strip()

    def __init__(self):
        self.__influx_client = InfluxDB.get_influx_client()

    @staticmethod
    def get_influx_client():
        """
        Get InfluxDB client instance
        :return: InfluxDB client instance, return the same client instance when creating a new InfluxDB instance.
        """
        if InfluxDB.__influx_client is None:
            print('[*] Creating new influx client instance')
            print("[*] INFLUX_VERSION=",'v1')
            print("[*] HOST=", InfluxDB.host)
            print("[*] PORT=", InfluxDB.port)
            print("[*] USER=", InfluxDB.username)
            print("[*] PASSWORD=", InfluxDB.password)
            print("[*] BUCKET=", InfluxDB.bucket)
            InfluxDB.__influx_client = InfluxDBClient(host=InfluxDB.host,
                                                    port=InfluxDB.port,
                                                    username=InfluxDB.username,
                                                    password=InfluxDB.password)
            # Created bucket if not exists
            InfluxDB.create_bucket(InfluxDB, InfluxDB.bucket)

        return InfluxDB.__influx_client

    def create_bucket(self, bucket_name):
        buckets = self.__influx_client.get_list_database()
        is_bucket_found = any(bucket['name'] == bucket_name for bucket in buckets)
        if not is_bucket_found:
            self.__influx_client.create_database(bucket_name)
            print('[*] Bucket [' + bucket_name + '] Created successfully')


    def write_data(self, measurement, fieldSet, tagSet=None):
        """
        Write Data To InfluxDB version 1
        :param measurement: The name of the measurement that you want to write your data to. The measurement is required in line protocol.
        :param fieldSet: The field(s) for your data point. Every data point requires at least one field in line protocol.
        Separate field key-value pairs with an equals sign = and no spaces
        :param tagSet: The tag(s) that you want to include with your data point. Tags are optional in line protocol.
        :return: None
        ----------------------------------------------------------------------------------------------------------------
        Line protocol syntax:

        <measurement>[,<tag_key>=<tag_value>,...] <field_key>=<field_value>[,<field_key>=<field_value>] [<timestamp>]
        ----------------------------------------------------------------------------------------------------------------
        Examples:

        Line protocol with tag         : weather,location=us-midwest temperature=82
        Line protocol without tag      : weather temperature=82
        Line protocol with many tags   : weather,location=us-midwest,continent=America temperature=82,waveHeight=2.1
        Line protocol with many fields : weather temperature=82,waveHeight=2.1
        ----------------------------------------------------------------------------------------------------------------
        """
        # concatenate comma before tag set if tagSet parameter is defined
        tagSet = ',' + tagSet if tagSet is not None else ''
        data = "{}{} {}".format(measurement, tagSet, fieldSet)
        # write the line protocol
        is_saved = self.__influx_client.write(data=data, 
                                            params= { "db": InfluxDB.bucket },
                                            protocol='line')
        if is_saved:
            print("[*] Writing data to [" + self.bucket + "] Bucket")
            print("[*] Data Saved: " + data + "\n\n")

        
    def close_connection(self):
        """
        Close Connection of InfluxDB Client
        :return: None
        """
        self.__influx_client.close()
