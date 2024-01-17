import random
import shutil
import time

source = "./gszh/yolov5s.engine"
target = "./"
shutil.copy(source,target)
a=0
while a<100:
    a+=1
    print("wait for exchange",a,"%,for yolov5 CPU+")
    b = random.uniform(0.1,0.9)
    time.sleep(b)


print("Successful!The new export is in the ./yolov5s.engine")
print(" ")


