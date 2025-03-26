import paho.mqtt.client as mqtt
import random
import datetime
import time
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.connect("localhost", 1884, 60)

now = datetime.datetime.now()
year = now.year-1
month = now.month-1
day=now.day-1
counter = 0

while True:

    if(counter==2):
        day=(day+1)%31
        print("day is: ", day)
        if(day==30):
            month=(month+1)%12
            print("month is: ", month)
            if(month==12): 
                year+=1
        counter= 0

    temp = random.randint(0, 100)
    humidity = random.randint(0, 100)

    payload = {
        "temp": temp,
        "hum": humidity,
        "year": year+1,
        "month": month+1,
        "day": day+1
    }

    client.publish("iot/native/launchpad/json", json.dumps(payload))
    time.sleep(1)
    counter+=1