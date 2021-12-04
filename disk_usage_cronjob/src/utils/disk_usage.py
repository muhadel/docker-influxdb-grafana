def getDiskUsageByPath(path='/'):
    # Get the disk usage statistics in bytes
    return shutil.disk_usage(path)


def getDf():
    df = os.popen("sshpass -p influxdb ssh -i /root/.ssh/id_rsa.pub influxdb@influxdb 'df -h'")
    i = 0
    while True:
        i = i + 1
        line = df.readline()
        print(line)
        if i == 2:
            return (line.split()[0:6])