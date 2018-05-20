#######################################################
##   Third class that have to SUBSCRIBE data         ##
##   to be placed on PC                              ##
#######################################################

import datetime
import paho.mqtt.client as paho
import requests
import json

class SubscribeData(object):

    @staticmethod
    def on_subscribe(client, userdata, mid, granted_qos):
        get_time = datetime.datetime.now()
        current_time =  get_time.strftime("%Y-%m-%d %H:%M:%S")
        print("Subscribed: " + str(mid) + " " + str(granted_qos))
        print ("at time: " + str(current_time))

    @staticmethod
    def on_message(client, userdata, msg):
        get_time = datetime.datetime.now()
        current_time =  get_time.strftime("%Y-%m-%d %H:%M:%S")
        print("message received ", str(msg.payload.decode("utf-8")))
        print ("at time: " + str(current_time))
        message_body = str(msg.payload.decode("utf-8"))


if __name__ == '__main__':
    # RUN THE SUBSCRIBE FOR GETTING THE TEMPERATURE AND HUMIDITY DATA
    try:
        file = open("config_file.json", "r")
        json_string = file.read()
        file.close()
    except:
        raise KeyError("***** SubscribeData: ERROR IN READING CONFIG FILE *****")

    config_json = json.loads(json_string)
    url = config_json["reSourceCatalog"]["url"]
    client = paho.Client()

    while True:
        try:
            respond = requests.get(url)
            json_format = json.loads(respond.text)
            AC_Topic = json_format["broker"]["AC_Topic"]
            print "PublishData:: BROKER VARIABLES ARE READY"
        except:
            print "PublishData: ERROR IN CONNECTING TO THE SERVER FOR READING BROKER TOPICS"

        try:
            client.on_subscribe = SubscribeData.on_subscribe
            client.on_message = SubscribeData.on_message
            client.connect('192.168.1.110', 1883)
            client.subscribe(str(AC_Topic), qos=1)
            client.loop_forever()
        except:
            print "SubscribeData: Problem in connecting to broker"

