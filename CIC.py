import subprocess, re
cmd = "netsh wlan show interfaces"
connected_network = subprocess.check_output(cmd, shell=True)                              #@9omw
ssid_line = re.search(b"SSID\\s+:\\s(.+)", connected_network)
print("Online" if ssid_line else "Offline")
