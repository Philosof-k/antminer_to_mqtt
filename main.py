#!/usr/bin/env python3

import socket
import json
import time
import configparser
import paho.mqtt.client as mqtt
#import os
#from sys import argv


config = configparser.ConfigParser()
config.read("config.ini")  # читаем конфиг
HOSTs = config["antminer"]["hosts"].split(',')
PORT = int(config["antminer"]["ipport"])
mqtt_ipaddress = config["mqtt"]["ipaddress"]
mqtt_user = config["mqtt"]["user"]
mqtt_pass = config["mqtt"]["pass"]
mqtt_topic = config["mqtt"]["topic"]

m = {"command": "stats"}
jdata = json.dumps(m)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
#        client.loop_start()
#        client.loop_start()
        print("connected OK Returned code=", rc)
        client.publish("antminer/status",payload="online", qos=0, retain=True)
        num = 0
        for x in HOSTs:
          num += 1
          client.publish("homeassistant/sensor/miner" + str(num) + "/temperature1/config", '{"availability":[{"topic":"antminer/status"}],"device":{"identifiers":["antminer_to_mqtt_miner' + str(num) + '"],"manufacturer":"Antminer","model":"S19j pro","name":"Miner' + str(num) + '"},"device_class":"temperature","enabled_by_default":true,"json_attributes_topic":"antminer/miner' + str(num) + '","name":"Miner' + str(num) + ' temp1","state_class":"measurement","state_topic":"antminer/miner' + str(num) + '","unique_id":"miner' + str(num) + '_temperature1","unit_of_measurement":"°C","value_template":"{{ value_json.STATS.1.temp2_1 }}"}', qos=1, retain=True)
          client.publish("homeassistant/sensor/miner" + str(num) + "/temperature2/config", '{"availability":[{"topic":"antminer/status"}],"device":{"identifiers":["antminer_to_mqtt_miner' + str(num) + '"],"manufacturer":"Antminer","model":"S19j pro","name":"Miner' + str(num) + '"},"device_class":"temperature","enabled_by_default":true,"json_attributes_topic":"antminer/miner' + str(num) + '","name":"Miner' + str(num) + ' temp2","state_class":"measurement","state_topic":"antminer/miner' + str(num) + '","unique_id":"miner' + str(num) + '_temperature2","unit_of_measurement":"°C","value_template":"{{ value_json.STATS.1.temp2_2 }}"}', qos=1, retain=True)
          client.publish("homeassistant/sensor/miner" + str(num) + "/temperature3/config", '{"availability":[{"topic":"antminer/status"}],"device":{"identifiers":["antminer_to_mqtt_miner' + str(num) + '"],"manufacturer":"Antminer","model":"S19j pro","name":"Miner' + str(num) + '"},"device_class":"temperature","enabled_by_default":true,"json_attributes_topic":"antminer/miner' + str(num) + '","name":"Miner' + str(num) + ' temp3","state_class":"measurement","state_topic":"antminer/miner' + str(num) + '","unique_id":"miner' + str(num) + '_temperature3","unit_of_measurement":"°C","value_template":"{{ value_json.STATS.1.temp2_3 }}"}', qos=1, retain=True)
          client.publish("homeassistant/sensor/miner" + str(num) + "/fan1/config", '{"availability":[{"topic":"antminer/status"}],"device":{"identifiers":["antminer_to_mqtt_miner' + str(num) + '"],"manufacturer":"Antminer","model":"S19j pro","name":"Miner' + str(num) + '"},"enabled_by_default":true,"json_attributes_topic":"antminer/miner' + str(num) + '","name":"Miner' + str(num) + ' FAN1","state_class":"measurement","state_topic":"antminer/miner' + str(num) + '","unique_id":"miner' + str(num) + '_fan1","unit_of_measurement":"rpm","value_template":"{{ value_json.STATS.1.fan1 }}"}', qos=1, retain=True)
          client.publish("homeassistant/sensor/miner" + str(num) + "/fan2/config", '{"availability":[{"topic":"antminer/status"}],"device":{"identifiers":["antminer_to_mqtt_miner' + str(num) + '"],"manufacturer":"Antminer","model":"S19j pro","name":"Miner' + str(num) + '"},"enabled_by_default":true,"json_attributes_topic":"antminer/miner' + str(num) + '","name":"Miner' + str(num) + ' FAN2","state_class":"measurement","state_topic":"antminer/miner' + str(num) + '","unique_id":"miner' + str(num) + '_fan2","unit_of_measurement":"rpm","value_template":"{{ value_json.STATS.1.fan2 }}"}', qos=1, retain=True)
          client.publish("homeassistant/sensor/miner" + str(num) + "/fan3/config", '{"availability":[{"topic":"antminer/status"}],"device":{"identifiers":["antminer_to_mqtt_miner' + str(num) + '"],"manufacturer":"Antminer","model":"S19j pro","name":"Miner' + str(num) + '"},"enabled_by_default":true,"json_attributes_topic":"antminer/miner' + str(num) + '","name":"Miner' + str(num) + ' FAN3","state_class":"measurement","state_topic":"antminer/miner' + str(num) + '","unique_id":"miner' + str(num) + '_fan3","unit_of_measurement":"rpm","value_template":"{{ value_json.STATS.1.fan3 }}"}', qos=1, retain=True)
          client.publish("homeassistant/sensor/miner" + str(num) + "/fan4/config", '{"availability":[{"topic":"antminer/status"}],"device":{"identifiers":["antminer_to_mqtt_miner' + str(num) + '"],"manufacturer":"Antminer","model":"S19j pro","name":"Miner' + str(num) + '"},"enabled_by_default":true,"json_attributes_topic":"antminer/miner' + str(num) + '","name":"Miner' + str(num) + ' FAN4","state_class":"measurement","state_topic":"antminer/miner' + str(num) + '","unique_id":"miner' + str(num) + '_fan4","unit_of_measurement":"rpm","value_template":"{{ value_json.STATS.1.fan4 }}"}', qos=1, retain=True)
          client.publish("homeassistant/sensor/miner" + str(num) + "/hash_5s/config", '{"availability":[{"topic":"antminer/status"}],"device":{"identifiers":["antminer_to_mqtt_miner' + str(num) + '"],"manufacturer":"Antminer","model":"S19j pro","name":"Miner' + str(num) + '"},"enabled_by_default":true,"json_attributes_topic":"antminer/miner' + str(num) + '","name":"Miner' + str(num) + ' HASH_5s","state_class":"measurement","state_topic":"antminer/miner' + str(num) + '","unique_id":"miner' + str(num) + '_hash_5s","unit_of_measurement":"TH","value_template":"{{ (value_json.STATS.1[\'GHS 5s\'] / 1000) | round(1) }}"}', qos=1, retain=True)
          client.publish("homeassistant/sensor/miner" + str(num) + "/hash_30m/config", '{"availability":[{"topic":"antminer/status"}],"device":{"identifiers":["antminer_to_mqtt_miner' + str(num) + '"],"manufacturer":"Antminer","model":"S19j pro","name":"Miner' + str(num) + '"},"enabled_by_default":true,"json_attributes_topic":"antminer/miner' + str(num) + '","name":"Miner' + str(num) + ' HASH_30m","state_class":"measurement","state_topic":"antminer/miner' + str(num) + '","unique_id":"miner' + str(num) + '_hash_30m","unit_of_measurement":"TH","value_template":"{{ (value_json.STATS.1.rate_30m / 1000) | round(1) }}"}', qos=1, retain=True)
#        logging.info("connected OK Returned code=" + str(rc))
#        client.subscribe("gate1/reply", qos=1)
    else:
        print("Bad connection Returned code=", rc)
#        logging.info("Bad connection Returned code=" + str(rc))

def on_disconnect(client, userdata, rc):
    if rc != 0:
#        client.loop_stop()
        print ("Unexpected MQTT disconnection. Will auto-reconnect")
        
        
        
client = mqtt.Client("antminer") #create new instance
client.username_pw_set(mqtt_user, mqtt_pass)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.will_set("antminer/status", payload="offline", qos=0, retain=True)
#client.on_subscribe = on_subscribe
#client.on_message = on_message
client.connect_async(mqtt_ipaddress) #connect to broker
#client.publish("test22","OFF")#publish
client.loop_start()

while True:
  num = 0
  for x in HOSTs:
  #  print (x)
    num += 1
    try:   
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((x, PORT))
        s.sendall(bytes(jdata,encoding="utf-8"))
        #time.sleep(2)
        data = ''
        while 1:
            chunk = s.recv(4026)
            if chunk:
                data += chunk.decode("utf-8") 
            else:
                break
        datajs = json.loads(data[:-1])
  #      print (json.dumps(datajs))
        client.publish(mqtt_topic + '/miner' + str(num), json.dumps(datajs), 1)
    except Exception:
  #  os.remove("test2.json")
  #    with open(NAMEs[x] + '.json', 'w') as outfile:
  #          print ("ex")
      client.publish(mqtt_topic + '/miner' + str(num), '{"STATUS": [{"STATUS": "S", "When": 1672756714, "Code": 70, "Msg": "CGMiner stats", "Description": "cgminer 1.0.0"}], "STATS": [{"BMMiner": "1.0.0", "Miner": "uart_trans.1.3", "CompileTime": "Tue Mar 29 14:31:43 CST 2022", "Type": "Antminer S19j Pro"}, {"STATS": 0, "ID": "BTM_SOC0", "Elapsed": 4815, "Calls": 0, "Wait": 0, "Max": 0, "Min": 99999999, "GHS 5s": 0, "GHS av": 0, "rate_30m": 0, "Mode": 2, "miner_count": 3, "frequency": 222, "fan_num": 4, "fan1": 0, "fan2": 0, "fan3": 0, "fan4": 0, "temp_num": 3, "temp1": 0, "temp2_1": 0, "temp2": 0, "temp2_2": 0, "temp3": 0, "temp2_3": 0, "temp_pcb1": "34-34-38-38", "temp_pcb2": "34-34-38-38", "temp_pcb3": "34-34-38-38", "temp_pcb4": "0-0-0-0", "temp_chip1": "39-39-43-43", "temp_chip2": "39-39-43-43", "temp_chip3": "39-39-43-43", "temp_chip4": "0-0-0-0", "temp_pic1": "24-24-28-28", "temp_pic2": "24-24-28-28", "temp_pic3": "24-24-28-28", "temp_pic4": "0-0-0-0", "total_rateideal": 40000.0, "rate_unit": "GH", "total_freqavg": 0, "total_acn": 378, "total rate": 0, "temp_max": 0, "no_matching_work": 0, "chain_acn1": 126, "chain_acn2": 126, "chain_acn3": 126, "chain_acn4": 0, "chain_acs1": " ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo", "chain_acs2": " ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo", "chain_acs3": " ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo", "chain_acs4": "", "chain_hw1": 0, "chain_hw2": 0, "chain_hw3": 0, "chain_hw4": 0, "chain_rate1": "0", "chain_rate2": "0", "chain_rate3": "0", "chain_rate4": "", "freq1": 0, "freq2": 0, "freq3": 0, "freq4": 0, "miner_version": "uart_trans.1.3", "miner_id": "no miner id now"}], "id": 1}', 1)
  #    outfile.close()
    finally:
      s.close
  time.sleep(10)