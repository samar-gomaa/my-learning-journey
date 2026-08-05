import sys
import time 
# Get the required test duration 
minutes = int(input("Enter test minutes: ")) 
seconds = int(input("Enter test seconds: ")) 
# Convert to total seconds 
total_seconds = (minutes * 60) + seconds
#invalid input recovery
if total_seconds<=0 or seconds>59:
    print("invalid test duration")
    sys.exit()
#max test duration   
if total_seconds>300:
    print("safety limit exceeded! test durationt capped to 05:00")
    total_seconds=300
#power state monitoring
while total_seconds>=0:
    minutes=total_seconds//60
    seconds=total_seconds%60
#normal operation
    if total_seconds>30:
        print(f"\rPOWER ON | Remaining:{minutes:02d} : {seconds:02d}", end="", flush=True,)
#stabilzation phase
    elif  total_seconds>10:
        print(f"\rSTABLIZING SYSTEM | Remaining:{minutes:02d} : {seconds:02d}", end="", flush=True,)
#cooldown phase
    else:
        print(f"\rCOOLDOWN PHASE| DO not touch | Remaining:{minutes:02d} : {seconds:02d}", end="", flush=True,)
    time.sleep(1)
    total_seconds-=1
print("\npower test completed successfully")