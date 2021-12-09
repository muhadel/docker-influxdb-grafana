# Pkg:
import schedule
from datetime import datetime
from utils import influxdb_v1, disk_usage


# Cron Job to run every 5 seconds.
def job():
    # Log cron job execution time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("[*] Cron job executed at " + dt_string)
    # Get disk usage by running Df command on the influxdb container
    stat = disk_usage.get_disk_usage()
    print("[*] Disk usage statistics: ", stat)
    influx_db = influxdb_v1.InfluxDB()
    influx_line_protocol = "total={},used={},free={}".format(stat[1], stat[2], stat[3])
    influx_db.write_data('disk_usage', influx_line_protocol, 'host=influxdb,Unit=Megabyte')

if __name__ == '__main__':
    try:
        print("[*] Initialize CronJob: ")
        
        schedule.every(5).seconds.do(job)
        while True:
            schedule.run_pending()
    except Exception as e:
        print("[*] Oops!", e.__class__, "occurred.")
        print(e)
