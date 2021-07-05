# RPi-HT22-Dynamo
Python code to connect a Raspberry Pi running an HT22 Temperature/Humidity sensor to DynamoDB in AWS

This code is based on a mixture of from sample code from AWS, and some code I found on the web, modified to work for my project. 

The AWS code corrected an error due to the web code being outdated. This works on a Raspbery Pi 4 with an HT-22 sensor. 

The code code is written in Python 3 and is sending sensor values to an AWS DynamoDB table named DHT. It sends a temperature and humidity reading at a set interval.

As seen in the code, I am using D4 as the GPIO pin for the sensor. It uses the Pi's 3.3 Volt power with a built in resistor that comes with the sensor that I found here: https://www.amazon.com/gp/product/B073F472JL/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1



