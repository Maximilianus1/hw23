import threading
import time
timeStart=time.time()

def create_file():
    time.sleep(1)
    file=open("file.txt","w")
    file.close()
    return "file created"
threads=[]
a=""
for i in range(100):
    local_thread = threading.Thread(target=create_file)
    local_thread.start()
    threads.append(local_thread)
print(str(threads))
timeFinish=time.time()
timeElapsed=timeFinish-timeStart
print(timeElapsed)
