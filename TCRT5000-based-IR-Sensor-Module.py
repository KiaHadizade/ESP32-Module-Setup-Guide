# ========================= "TCRT5000 Infrared Reflective Line Track Sensor Module" ========================= #


from machine import Pin
import time

# Connect OUT pin of sensor to GPIO 23
ir_sensor = Pin(23, Pin.IN)

while True:
    if ir_sensor.value() == 0:
        print("Object detected!")
    else:
        print("No object.")
    time.sleep(0.5)










# ================= test =================

# from machine import Pin
# import time

# ir_sensor = Pin(23, Pin.IN)

# while True:
#     print("IR raw value:", ir_sensor.value())
#     time.sleep(0.5)

# ================= test =================