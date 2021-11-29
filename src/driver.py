
#from events.traffic_count import traffic_count
import importlib
import threading
import time
from queue import Queue

def handle_event(event_name,workers,messageq,todo):
    if event_name != 'stop':
        event = importlib.import_module(f"events.{event_name}")
        worker = threading.Thread(target=event.process,args=(messageq,todo,))
        workers.append(worker)
        worker.start()
    return True

def load_event(todo):
    pass

def raise_event(todo,eq,messageq):
    if not todo.empty():
        eq.append(todo.get())
        with todo.mutex:
            todo.queue.clear()
    if not messageq.empty():
        todo.put("publish")
    return True

def driver():
    messageq = Queue()
    todo = Queue()
    todo.put('subscribe')
    eq = []
    workers = []
    next_event = None
    while next_event != "stop":
        raise_event(todo,eq,messageq)
        if len(eq)!=0:
            next_event = eq.pop()
            handle_event(next_event,workers,messageq,todo)
    for work in workers:
        work.do_run = False
        work.join()


# event = importlib.import_module("events.traffic_count")
# event.process
driver()