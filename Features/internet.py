import speedtest

def bytes_to_mb(bytes):
  try:
    KB = 1024 # One Kilobyte is 1024 bytes
    MB = KB * 1024 # One MB is 1024 KB
    return int(bytes/MB)
  except:
    return "Unable to get internet speed"

def get_speed():
  try:
    st = speedtest.Speedtest()
    download_speed = st.download()
    upload_speed = st.upload()
    ping = st.results.ping
    download_speed_mbps = download_speed / 10**6
    upload_speed_mbps = upload_speed / 10**6

    return "You have a download and upload speed of "+str(bytes_to_mb(download_speed))+" MBPS, and "+str(bytes_to_mb(upload_speed))+" MBPS respectively. Your Pings are "+str(ping)+" MS"
  except:
    return "Unable to get internet speed"