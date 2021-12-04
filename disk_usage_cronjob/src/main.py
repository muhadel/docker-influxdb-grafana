# Pkg:
import schedule
import time
import os
from datetime import datetime
# from dotenv import load_dotenv
import shutil
from utils import influxdb2, disk_usage


# Cron Job to run every 5 minutes.
def job():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("I'm working...", dt_string)
    rootDisk = disk_usage.getDf()
    print("rootDisk: ==>", rootDisk)

    stat = disk_usage.getDiskUsageByPath()
    print("Disk usage statistics:")
    total, used, free = stat
    print(stat)
    print(total, used, free)
    print("=========InfluxDB=============")
    influxDB = influxdb2.InfluxDB()
    print('List databases...')
    print(influxDB.listDatabases())


if __name__ == '__main__':
    # try:
    #     print("Initialize CronJob schedule...")
    #     if True:
    #         schedule.every(5).seconds.do(job)
    #     while True:
    #         schedule.run_pending()
    #         time.sleep(1)
    # except Exception as e:
    #     print("Oops!", e.__class__, "occurred.")
    #     print(e)

    print('Start App')
    print("=========InfluxDB=============")
    influxDB = influxdb2.InfluxDB()
    print('Write Data...')
    # print(influxDB.writeData('test', 'temperature=82,waveHeight=2.1'))

    influxDB.executeQuery()
