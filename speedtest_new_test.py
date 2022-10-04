"""module for running a new speedtest test"""
import time
import speedtest
import math
import bitmath

def convert_size(size_bytes):
   #size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, "Mbps")

def attempt(attemps:int=1,sleep_time:int=1, Try:bool=True, max_attempt_limit=5, totalAttemps=1, debug_sleep:int=0, debug_flag:bool=False):
    if debug_sleep:
        debug_flag = True
        sleep_time = debug_sleep
    connected=False
    while not connected:
        print(f"Connection attemp {attemps}", end="\r", flush=True)
        if debug_flag:
            with open("_debug_retry_attempts_amount.txt", "w") as f:
                f.write(str(attemps))
                f.close()
        try:
            speedtest.Speedtest()
        except speedtest.ConfigRetrievalError:
            connected = False
            attemps+=1
            if attemps < max_attempt_limit:
                sleep_time = max_attempt_limit
            time.sleep(sleep_time)
            attempt(attemps)
        connected = True
        print("\nCONNECTED\n")
        break
    return speedtest.Speedtest()
st = attempt(debug_sleep=0)
servers = st.get_best_server()
print("Checking Down Speeds...")
down_bit = st.download(threads=None)
down_kb = bitmath.Bit(down_bit)
print("Done Checking Down Speeds...")
print("Checking Up Speeds...")
up_bit = st.upload(threads=None, pre_allocate=True)
up_kb = bitmath.Bit(up_bit)
print("Done Checking Up Speeds...")
print()
print(f"{down_bit = }")
print(f"{down_kb.to_Mb() = }")
print(f"{up_bit = }")
print(f"{  up_kb.to_Mb() = }")
