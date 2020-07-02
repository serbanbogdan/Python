'''
Module necesare win10toast, wmi
Open Hardware Monitor deschis
'''
from win10toast import ToastNotifier
import wmi

to_toast = ""

# Get temp data from Open Hardware Monitor
w = wmi.WMI(namespace="root\OpenHardwareMonitor")
temperature_infos = w.Sensor()
for sensor in temperature_infos:
    if sensor.SensorType==u'Temperature' and (sensor.Name==u'GPU Core' or sensor.Name==u'CPU Package'):
        to_toast += str(sensor.Value) + ' ° C  ' + sensor.Name + "\n"

# Print Windows 10 toast
toaster = ToastNotifier()
toaster.show_toast(to_toast," ",duration=30)
