from pymodbus.client.sync import ModbusSerialClient
import time
import random

client = ModbusSerialClient(method="rtu", port="COM5", stopbits=1, bytesize=8, parity='N', baudrate=9600)



while True:

    try:
        client.connect()
        data = random.randint(20, 80)
        result_ = client.write_registers(3546, data , unit=1)
        value = result_
        print(value)
        client.close()
        time.sleep(5)
    except:
        time.sleep(1)
        

