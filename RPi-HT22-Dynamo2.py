#CopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_dht
import boto3
import threading
from datetime import datetime, timedelta

dhtDevice = adafruit_dht.DHT22(board.D4)
# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

class MyDb(object):

    time.sleep(60)

# Initialize the dht22 device, with data pin connected to 4:
    dhtDevice = adafruit_dht.DHT22(board.D4)

    def __init__(self, Table_Name='DHT'):
        self.Table_Name=Table_Name

        self.db = boto3.resource('dynamodb')
        self.table = self.db.Table(Table_Name)

        self.client = boto3.client('dynamodb')

    try:
        def put(self, DHT22_ID='' , Temperature='', Humidity='', ReadTime='', TTL=''):
            self.table.put_item(
                    Item={
                    'DHT22_ID':DHT22_ID,
                    'Temperature':Temperature,
                    'Humidity' :Humidity,
                    'ReadTime' :ReadTime,
                    'TTL' :TTL
            }
        )
    except:
        print("could not write to dynamo")

    def describe_table(self):
        response = self.client.describe_table(
            TableName='DHT'
        )
        return response

    @staticmethod
    def sensor_value():

        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity

        if humidity is not None and temperature_f is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature_f, humidity))
        else:
            print('Failed to get reading. Try again!')
        return temperature, humidity


def main():
    try:
        global counter
        threading.Timer(interval=3600, function=main).start()
        obj = MyDb()
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        now = datetime.now()
        epoch_time = int(time.time())
        orig = datetime.fromtimestamp(epoch_time)
        new = orig + timedelta(days=7)
        obj.put(DHT22_ID=(str(counter)+ " : " + str(now.strftime("%m-%d-%Y %H:%M:%S"))), Temperature=str(temperature_f), Humidity=str(humidity), ReadTime=str(now.strftime("%m-%d-%Y %H:%M:%S")), TTL=int(new.timestamp()))
        counter = counter + 1
        print("Uploaded Sample on Cloud T:{},H{} ".format(temperature_f, humidity))
    except:
        print("Something went wrong")

if __name__ == "__main__":
    global counter
    counter = 0
    main()
