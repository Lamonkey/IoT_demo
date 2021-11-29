import paho.mqtt.client as paho
def process(q,todo):
    broker="127.0.0.1"
    port=1883
    def on_publish(client,userdata,result):             #create function for callback
        print("data published \n")
        pass
    client1= paho.Client("control1")                           #create client object
    client1.on_publish = on_publish                          #assign function to callback
    client1.connect(broker,port)                                 #establish  connection
    while not q.empty():
        message = q.get(block=True)
        topic = message[0]
        load = message[1]
        print(f"topic:{topic},load:{load}")
        client1.publish(topic,load) 
    print("publish exist")  

