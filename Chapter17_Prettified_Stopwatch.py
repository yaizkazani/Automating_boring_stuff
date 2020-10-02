#! python3
# Lap #1: 3.56 (3.56)
# Lap #2: 8.63 (5.07)
# Lap #3: 17.68 (9.05)
# Lap #4: 19.11 (1.43)
# get start timestamp
# lap timestamp = start timestamp
# when user press enter print current timestamp - last lap timestamp
# update lap timestamp
# accumulate data somewhere
# handle ctrl+C exception, at this point copy data to pyperclip

import time, pyperclip

print("Started")
start_time = time.time()
lap_time = start_time
lap = 1
clip_str = ""
while 1:
    try:
        input()
        s = f"Lap #{lap}:" + f"{round(time.time() - start_time, 2)}".center(8, " ") + f"({round(time.time() - lap_time, 2)})"
        clip_str += str(s + "\n")
        print(s, end="")
        lap_time = time.time()
        lap += 1
    except KeyboardInterrupt:
        pyperclip.copy(clip_str)
        print("KeyboardInterrupt exception caught, exiting, data copied to clipboard")
        break


