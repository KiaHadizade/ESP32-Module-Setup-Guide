# ESP32 MicroPython Setup Guide

A beginner-friendly guide to setting up MicroPython on your ESP32 development board using Thonny IDE

## 🛠️ Requirements

- ESP32 development board (e.g., ESP32 DevKit V1)
- Micro USB cable
- A tool to communicate with the board (like Thonny IDE or another supported IDE)
- MicroPython firmware flashed on the ESP32 board
- Internet connection

## 🔌 Connect ESP32 to PC

1. Plug the ESP32 into your computer using the micro USB cable
2. Make sure the correct driver is installed (e.g., CP210x or CH340, depending on your board)[^1]

## 🔧 Flash MicroPython Firmware to the ESP32

### 1. Download firmware

Go to the official MicroPython site:
👉 [https://micropython.org/download/esp32/](https://micropython.org/download/esp32/)
Download the latest `.bin` firmware file
> [!NOTE]
> Download the correct firmware version for your ESP32 board (e.g., esp32-xxxxxx-v1.22.x.bin)

### 2. Install esptool.py (tool to flash firmware)

Make sure you have Python installed on your computer. Then install esptool in your terminal or command prompt:
``` bash
$ pip install esptool
```

### 3. Erase existing firmware (optional but recommended)

Identify the serial port:
- On **Windows**: something like `COM3`
- On **Linux/macOS**: something like `/dev/ttyUSB0` or `/dev/tty.SLAB_USBtoUART`

Then run:
``` bash
$ python -m esptool --port PORT erase_flash
```

> [!NOTE]
> Replace PORT with your actual port (like COM3)

### 4. Flash MicroPython firmware

Run the following:
``` bash
$ python -m esptool --chip esp32 --port PORT --baud 460800 write_flash -z 0x1000 firmware.bin
```

> [!NOTE]
> Replace PORT and firmware.bin with your actual values

## 📥 Install Thonny IDE

Download and install the Thonny IDE from the official website:
🔗 [https://thonny.org/](https://thonny.org/)

**With Thonny**:
- Install and open it
- Go to **Tools** > **Options** > **Interpreter**
    - **Interpreter**: MicroPython (ESP32)
    - **Port**: Select the port your ESP32 is on (COM3)
- Now you should see a prompt like this in shell (REPL):
`$ MicroPython v1.22.x on 2025-xx-xx; ESP32 module with ESP32`

> [!NOTE]
> Easy and lightweight IDE with built-in MicroPython support

## 🚀 Test sample code

Once you're at the REPL, you can run this script for LED blink:

``` python
from machine import Pin
import time

led = Pin(2, Pin.OUT)

while True:
    led.value(not led.value())
    time.sleep(0.5)
```
Onboard LED should now blink every half second

> [!TIP]
> [^1] Finding the COM port your ESP32 is using:<br>
> Press Win + X → Click Device Manager<br>
> Expand Ports (COM & LPT)<br>
> Look for something like:<br>
> `Silicon Labs CP210x USB to UART Bridge (COM3)`<br>
> Note the COM port number (e.g., COM3 or COM4). That’s what you’ll use in the --port option for esptool.py

> Downloaded zip file named ESP32-ChatGPT-V2-main from [Github](https://github.com/techiesms/ESP32-ChatGPT-V2)<br>
> Downloaded zip file named KALO-ESP32-Voice-Assistant-main from [Github](https://github.com/kaloprojects/KALO-ESP32-Voice-Assistant)<br>
> Downloaded zip file named ESP32-audioI2S-master from [Github](https://github.com/schreibfaul1/ESP32-audioI2S)