import datetime 
import time

now = datetime.datetime.now()

print(f"Starting job: {now}")

time.sleep(10)

now = datetime.datetime.now()

print(f"Finished job: {now}")
