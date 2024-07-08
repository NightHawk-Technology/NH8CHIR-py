## NH8CHIR-py

ใน Library จะมี 2 ไฟล์หลักคือ
- nh8chir.py
- i2c_scan.py

โดย `nh8chir.py` คือ Library สำหรับเรียกใช้งานเซ็นเซอร์ NH8CHIR และ `i2c_scan.py` ใช้สำหรับค้นหาอุปกรณ์ที่เขื่อมต่อการสื่อสารผ่าน I2C
<hr>

## ตัวอย่างการใช้งาน nh8chir.py

### การเรียกใช้งานเซ็นเซอร์
```Python
from machine import I2C, Pin
from lib.nh8chir import NH8CHIR
import time

i2c0 = I2C(0, scl=Pin(1), sda=Pin(0))
sensor = NH8CHIR(i2c0, 0x48)          #เปลี่ยนได้ตาม Address ของเซ็นเซอร์

sensorValues = [0,0,0,0,0,0,0,0]

while True:
  for i in range(0,8):
    sensorValues[i] = sensor.read(i)

  print(sensorValues)
  time.sleep(0.01)
```
<hr>

## ตัวอย่างการใช้งาน i2c_scan.py

```Python
from machine import I2C, Pin
from lib.nh8chir import i2c_scan
import time

i2c_scan.scan(0)      #0 หมายถึงช่อง I2C ที่ 0 (GP0, GP1)
```

<hr>
