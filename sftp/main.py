import paramiko
import datetime


current_date = datetime.datetime.now()
filter_current_date = current_date.strftime("%Y%m%d")

# create ssh client
ssh_client = paramiko.SSHClient()

# remote server credentials
host = ""
username = ""
password = ""
port = 22
remote_dir = "Outbound"
local_dir = "/tmp"

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host, port=port,
                   username=username, password=password)
ssh_client.connect(hostname=host, port=port,
                   username=username, password=password)


ftp = ssh_client.open_sftp()
files = ftp.listdir(f"/{remote_dir}")

try:
    for i in files:
        if filter_current_date in i:
            print(f"Downloading file {i} ...")
            ftp.get(f"{remote_dir}/{i}",
                    f"{local_dir}/{i}", callback=None, max_concurrent_prefetch_requests=None)

except FileNotFoundError as err:
    print(
        f"File: was not found on the source server")

ftp.close()
ssh_client.close()
