"""module for running a new speedtest test"""
import time
import speedtest
import math

def convert_size(size_bytes):
   #size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, "Mbps")

def attempt(attemps:int=0, Try:bool=True, max_attempt_limit=5, totalAttemps=1):
    connected=False
    while not connected:
        print("Connecting")
        try:
            st = speedtest.Speedtest()
        except speedtest.ConfigRetrievalError:
            connected = False
        connected = True
        print("CONNECTED")
        break
    return st
    
st = attempt()
servers = st.get_best_server()
print("Checking Down Speeds...")
down = st.download(threads=None)
print("Done Checking Down Speeds...")
print("Checking Up Speeds...")
up = st.upload(threads=None, pre_allocate=True)
print("Done Checking Up Speeds...")
print(f"{down = }")
print()
print(f"{up = }")
