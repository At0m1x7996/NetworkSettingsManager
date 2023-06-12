import time
import ctypes
import wmi

if not ctypes.windll.shell32.IsUserAnAdmin():
    print('Not enough priviledge, restarting...')
    import sys
    ctypes.windll.shell32.ShellExecuteW(
        None, 'runas', sys.executable, ' '.join(sys.argv), None, None)
else:
    print('Elevated privilege acquired')

# Obtain network adaptors configurations
nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

# First network adaptor
nic = nic_configs[1]

ip = "10.0.0.160"
sm = "255.0.0.0"
gw = "10.0.0.1"

nic.EnableStatic(IPAddress=[ip],SubnetMask=[sm])
nic.SetGateways(DefaultIPGateway=[gw])

print(nic.DHCPEnabled)


print(wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)[1].IpAddress)

# for nic in nic_configs:
    # print("---------------------------------------------------------------------------------------------------------")
    # print(nic.Description)

 

# IP address, subnetmask and gateway values should be unicode objects
#ip = u'192.168.0.11'
#subnetmask = u'255.255.255.0'
#gateway = u'192.168.0.1'

# Set IP address, subnetmask and default gateway
# Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
