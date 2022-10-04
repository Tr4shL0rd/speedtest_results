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

def attempt(attemps:int=0, Try:bool=True, max_attempt_limit=5, totalAttemps=0):
    if Try:
        print("Connecting...")
        print(f"DEBUG: attempt #{totalAttemps}")
        try:
            while not speedtest.Speedtest():
                pass
        except speedtest.ConfigRetrievalError:
            totalAttemps+=1
            if attemps < max_attempt_limit:
                attemps+=1
            else:
                attemps = max_attempt_limit
            print(f"Connection Failed...\nTrying again in {attemps} seconds.\n")
            time.sleep(attemps)
            attempt(attemps,totalAttemps=totalAttemps)
    return speedtest.Speedtest()
    
st = attempt(totalAttemps=0)
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
