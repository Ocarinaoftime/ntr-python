from pyremoteplay import RPDevice
from pyremoteplay.receiver import QueueReceiver

ip = "172.24.1.220"
device = RPDevice(ip)
device.get_status()
user = device.get_users()
receiver = QueueReceiver()
device.connect()
device.wait_for_session()