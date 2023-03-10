#!/usr/bin/env python3

import socket
import json
import time
import configparser
import paho.mqtt.client as mqtt
#import os
#from sys import argv

#script, ip = argv

#print ("Ётот скрипт называетс¤: ", script)
#print ("«начение первой переменной: ", first)

config = configparser.ConfigParser()
config.read("config.ini")  # читаем конфиг
HOSTs = config["antminer"]["hosts"].split(',')
PORT = str(config["antminer"]["ipport"])
mqtt_ipaddress = config["mqtt"]["ipaddress"]
mqtt_user = config["mqtt"]["user"]
mqtt_pass = config["mqtt"]["pass"]
mqtt_topic = config["mqtt"]["topic"]

#print (HOSTs)
#print (HOSTs[0])


#HOSTs = ["192.168.84.81", "192.168.84.85", "192.168.84.83"] # Antminer IP
#NAMEs = ["miner1", "miner2", "miner3"]
#NUM = [0, 1, 2]
#PORT = 4028        

m = {"command": "stats"}
jdata = json.dumps(m)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
#        client.loop_start()
#        client.loop_start()
        print("connected OK Returned code=", rc)
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
#client.on_subscribe = on_subscribe
#client.on_message = on_message
client.connect_async(mqtt_ipaddress) #connect to broker
#client.publish("test22","OFF")#publish
client.loop_start()

num = 0
for x in HOSTs:
#  print (x)
  num += 1
  try:   
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect((x, 4028))
      s.sendall(bytes(jdata,encoding="utf-8"))
      time.sleep(2)
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
#      with open(NAMEs[x] + '.json', 'w') as outfile:
#          json.dump(datajs, outfile)
#      outfile.close()
#  os.rename('test.json', 'test2.json')
  except Exception:
#  os.remove("test2.json")
#    with open(NAMEs[x] + '.json', 'w') as outfile:
          print ("ex")
          client.publish(mqtt_topic + '/miner' + str(num), '{"STATUS": [{"STATUS": "S", "When": 1672756714, "Code": 70, "Msg": "CGMiner stats", "Description": "cgminer 1.0.0"}], "STATS": [{"BMMiner": "1.0.0", "Miner": "uart_trans.1.3", "CompileTime": "Tue Mar 29 14:31:43 CST 2022", "Type": "Antminer S19j Pro"}, {"STATS": 0, "ID": "BTM_SOC0", "Elapsed": 4815, "Calls": 0, "Wait": 0, "Max": 0, "Min": 99999999, "GHS 5s": 0, "GHS av": 0, "rate_30m": 0, "Mode": 2, "miner_count": 3, "frequency": 222, "fan_num": 4, "fan1": 0, "fan2": 0, "fan3": 0, "fan4": 0, "temp_num": 3, "temp1": 0, "temp2_1": 0, "temp2": 0, "temp2_2": 0, "temp3": 0, "temp2_3": 0, "temp_pcb1": "34-34-38-38", "temp_pcb2": "34-34-38-38", "temp_pcb3": "34-34-38-38", "temp_pcb4": "0-0-0-0", "temp_chip1": "39-39-43-43", "temp_chip2": "39-39-43-43", "temp_chip3": "39-39-43-43", "temp_chip4": "0-0-0-0", "temp_pic1": "24-24-28-28", "temp_pic2": "24-24-28-28", "temp_pic3": "24-24-28-28", "temp_pic4": "0-0-0-0", "total_rateideal": 40000.0, "rate_unit": "GH", "total_freqavg": 0, "total_acn": 378, "total rate": 0, "temp_max": 0, "no_matching_work": 0, "chain_acn1": 126, "chain_acn2": 126, "chain_acn3": 126, "chain_acn4": 0, "chain_acs1": " ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo", "chain_acs2": " ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo", "chain_acs3": " ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo ooo", "chain_acs4": "", "chain_hw1": 0, "chain_hw2": 0, "chain_hw3": 0, "chain_hw4": 0, "chain_rate1": "0", "chain_rate2": "0", "chain_rate3": "0", "chain_rate4": "", "freq1": 0, "freq2": 0, "freq3": 0, "freq4": 0, "miner_version": "uart_trans.1.3", "miner_id": "no miner id now"}], "id": 1}', 1)
#    outfile.close()
  finally:
    s.close
#    outfile.close()
print ("1")
#time.sleep(5)
#print ("2")

#print (json.dumps(datajs))