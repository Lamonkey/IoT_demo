import os
import shutil
def process(q,todo):
    source = '/Users/lamonkey/Desktop/op_destination/events/'
    destination = '/Users/lamonkey/Desktop/IoT_demo/src/events'
    files = os.listdir(source)

    for fname in files:
        
        shutil.copy2(os.path.join(source,fname), destination)
    print("update exist")  
process(None,None)

