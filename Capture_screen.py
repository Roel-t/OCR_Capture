
import mss
import mss.tools


with mss.mss() as sct:
    # The screen part to capture
    monitor = {"top": 589, "left": 65, "width": 540, "height": 450}
    output = "images/b.png".format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)