from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from utils.config import config


class InfluxDB:
    __client = None
    url = config.get('INFLUXDB_URL')
    token = config.get('INFLUXDB_ADMIN_TOKEN')
    org = config.get('INFLUXDB_ORG')
    bucket = config.get('INFLUXDB_BUCKET')

    @staticmethod
    def getInstance():
        """
        Get InfluxDB client instance
        :return: InfluxDB client instance, return the same client instance when creating a new InfluxDB instance.
        """
        print("config.get('INFLUXDB_URL')", config.get('INFLUXDB_URL'))
        if InfluxDB.__client is None: InfluxDB.__client = InfluxDBClient(url=InfluxDB.url, token=InfluxDB.token,
                                                                         org=InfluxDB.org)
        return InfluxDB.__client

    def writeData(self, measurement, fieldSet, tagSet=None):
        """
        Write Data To InfluxDB version 2
        :param measurement: The name of the measurement that you want to write your data to. The measurement is required
                            in line protocol.
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
        # define influxDB write endpoint to write data
        write_api = self.getInstance().write_api(write_options=SYNCHRONOUS)
        # concatenate comma before tag set if tagSet parameter is defined
        tagSet = ',' + tagSet if tagSet is not None else ''
        data = "{}{} {}".format(measurement, tagSet, fieldSet)
        write_api.write(self.bucket, self.org, data)
        print("[*] Writing data: " + data)

    def executeQuery(self):
        """
        Execute Query on Influx DB
        This method returns all data in all measurements by specifying bucket name in the query (Bucket_Name=default)
        :return: None
        """
        query = 'from(bucket: "default") |> range(start: -1h)'
        tables = self.getInstance().query_api().query(query, org=self.org)
        print(tables)
        for table in tables:
            for record in table.records:
                print(record)

    def closeConnection(self):
        """
        Close Connection of InfluxDB Client
        :return: None
        """
        self.getInstance().close()
