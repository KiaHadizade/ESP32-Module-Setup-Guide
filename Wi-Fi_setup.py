import network
import time

# ===== Wi-Fi Config ===== #
SSID = "YOUR_SSID_NAME"
PASSWORD = "YOUR_PASSWORD"


# ===== Connect to Wi-Fi ===== #
def connect_wifi():
    # Create a station interface
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    print("Connecting to Wi-Fi...", end="")

    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
    print("\nConnected! Network config:", wlan.ifconfig()) # Once connected, wlan.ifconfig() returns a tuple: (ip, subnet_mask, gateway, dns)


# ===== Disconnect from Wi-Fi ===== #
def disconnect_wifi():
    wlan = network.WLAN(network.STA_IF)
    if wlan.isconnected():
        wlan.disconnect()
        print("Wi-Fi disconnected.")
    else:
        print("Wi-Fi is not connected.")

    # Optional: deactivate the Wi-Fi interface if you want to fully shut it down
    # wlan.active(False)
    # print("Wi-Fi interface deactivated.")


connect_wifi()
# disconnect_wifi()