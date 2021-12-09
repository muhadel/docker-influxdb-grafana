from influxdb import InfluxDBClient
from utils.config import config


class InfluxDB:
    __influx_client = None
    host = config.get('INFLUXDB_CONTAINER_HOST')
    port = config.get('INFLUXDB_CONTAINER_PORT')
    username = config.get('INFLUXDB_USERNAME')
    password = config.get('INFLUXDB_PASSWORD')
    # url = config.get('INFLUXDB_URL')
    # token = config.get('INFLUXDB_ADMIN_TOKEN')
    # org = config.get('INFLUXDB_ORG')
    bucket = config.get('INFLUXDB_BUCKET')

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
            print("[*]", InfluxDB.url, InfluxDB.token, InfluxDB.org)
            InfluxDB.__influx_client = InfluxDBClient(host=InfluxDB.host, port=InfluxDB.port, username=InfluxDB.username, password=InfluxDB.password)
            print("CLient", InfluxDB.__influx_client)

        # Created bucket if not exists
        InfluxDB.create_bucket(InfluxDB, InfluxDB.bucket)

        return InfluxDB.__influx_client

    def create_bucket(self, bucket_name):
        print('[*****] Try to create bucket', bucket_name)
        buckets = self.__influx_client.get_list_database()
        if bucket_name not in buckets:
            self.__influx_client.create_database(bucket_name)
            print('[*] Bucket [' + bucket_name + '] Created successfully')

            
        

    def write_data(self, measurement, fieldSet, tagSet=None):
        """
        Write Data To InfluxDB version 2
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
        self.__influx_client.write(data=data,params={"db": InfluxDB.bucket}, protocol='line')
        print("[*] Writing data to [" + self.bucket + "] Bucket")
        print("[*] Data Saved: " + data + "\n\n")
        

    # def execute_query(self):
    #     """
    #     Execute Query on Influx DB
    #     This method returns all data in all measurements by specifying bucket name in the query (Bucket_Name=default)
    #     :return: None
    #     """
    #     query = 'from(bucket: "default") |> range(start: -1h)'
    #     tables = self.__influx_client.query_api().query(query, org=self.org)
    #     print(tables)
    #     for table in tables:
    #         for record in table.records:
    #             print(record)

    def close_connection(self):
        """
        Close Connection of InfluxDB Client
        :return: None
        """
        self.__influx_client.close()
