#update code in src
import paho.mqtt.subscribe as subscribe
import threading


def process(in_q,todo):
    t = threading.currentThread()
    while getattr(t,'do_run',True):
        msg = subscribe.simple("event", hostname="127.0.0.1")
        todo.put(msg.payload.decode('utf-8'))
    print("process exist..")