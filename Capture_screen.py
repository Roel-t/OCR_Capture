
import mss
import mss.tools

#15 seconds
with mss.mss() as sct:
    # The screen part to capture
    monitor = {"top": 300, "left": 65, "width": 800, "height": 710}
    output = "images/f.png".format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)