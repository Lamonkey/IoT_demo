import random
import time
import threading
def process(q,todo):
    t = threading.currentThread()
    while getattr(t,'do_run',True):
        q.put(('traffic_count',random.randint(1,100)))
        time.sleep(1.2)
    print("traffic_count exist..")
