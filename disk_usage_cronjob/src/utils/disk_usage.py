import os
from utils.config import config


def get_disk_usage():
    """
    Get Disk Usage
    --------------
    This method executes 'df' unix command on influxdb container
    using 'ssh' command to navigate from the current container(disk_usage_cronjob) to another container (influxdb)

    :return: Array of the result of 'df' unix command for root directory '/'

    Return example  : ['overlay', '8376300', '3788776', '4587524', '46%', '/']
    Which represent : [FILE_SYSTEM, TOTAL_DISK_IN_MB, USED_DISK_IN_MB, FREE_DISK_IN_MB, USAGE_PERCENTAGE, MOUNTED_ON]


    """
    command = "sshpass -p {} ssh -i /root/.ssh/id_rsa.pub {}@{} 'df'".format(
        config.get('INFLUXDB_CONTAINER_PASSWORD'),
        config.get('INFLUXDB_CONTAINER_USER'),
        config.get('INFLUXDB_CONTAINER_HOST'))
    df = os.popen(command)
    i = 0
    while True:
        i = i + 1
        line = df.readline()
        print(line)
        if i == 2:
            return line.split()[0:6]