# Pkg:
import schedule
import time
from datetime import datetime
from utils import influxdb_v2, disk_usage


# Cron Job to run every 5 minutes.
def job():
    # Log cron job execution time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("[*] Cron job executed at " + dt_string)
    # Get disk usage by running Df command on the inflfuxdb container
    stat = disk_usage.getDiskUsage()
    print("[*] Disk usage statistics: ", stat)
    influx_db = influxdb_v2.InfluxDB()
    influx_line_protocol = "total={},used={},free={}".format(stat[1], stat[2], stat[3])
    influx_db.writeData('disk_usage', influx_line_protocol, 'host=influxdb,Unit=Megabyte')


if __name__ == '__main__':
    try:
        print("[*] Initialize CronJob: ")
        if True:
            schedule.every(5).seconds.do(job)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        print("[*] Oops!", e.__class__, "occurred.")
        print(e)
