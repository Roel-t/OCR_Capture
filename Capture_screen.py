import cv2

import mss
import mss.tools
import schedule
import time

import time

#VARIABLES

#image name is timestamp
current_time = ""
elapse_time = 5


def job():
    current_time = time.strftime("%H%M")
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": 300, "left": 65, "width": 825, "height": 710}
        output = "images/"+current_time+".png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(output)

schedule.every(elapse_time).minutes.do(job)

#CTRL + F2 to stop it
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    pass

