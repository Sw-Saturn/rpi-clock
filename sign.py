#!/usr/bin/env python
import time
from samplebase import SampleBase
from rgbmatrix import graphics
from datetime import datetime
from PIL import Image
import subprocess


class ImageScroller(SampleBase):
    def __init__(self, *args, **kwargs):
        super(ImageScroller, self).__init__(*args, **kwargs)
        self.parser.add_argument("-i", "--image", help="The image to display", default="../../../examples-api-use/runtext.ppm")

    def run(self):
        if not 'image' in self.__dict__:
            self.image = Image.open(self.args.image).convert('RGB')
        self.image.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)

        double_buffer = self.matrix.CreateFrameCanvas()
        img_width, img_height = self.image.size
        font = graphics.Font()
        font_time = graphics.Font()
        # font.LoadFont("../../../fonts/mplus_h12r.bdf")
        font_time.LoadFont("./fonts/21-Adobe-Helvetica.bdf")
        # font.LoadFont("../../../fonts/15-Adobe-Helvetica.bdf")
        font.LoadFont("./fonts/16-Adobe-Helvetica-Bold.bdf")

        textColor = graphics.Color(245, 0, 111)
        timeColor = graphics.Color(61, 147, 215)
        pos = double_buffer.width

        # let's scroll
        xpos = -128
        while True:
            xpos += 2
            if (xpos > img_width):
                exit()
            d = datetime.now()
            h = (" " + str(d.hour))[-2:]
            time_text = d.strftime("%H:%M:%S")
            
            double_buffer.Clear()
            # len = graphics.DrawText(offscreen_canvas, font, 4, 12, textColor, date_text)
            #len1 = graphics.DrawText(double_buffer, font_time, 14, 30, timeColor, time_text)

            double_buffer.SetImage(self.image, -xpos)
            #double_buffer.SetImage(self.image, -xpos + img_width)

            double_buffer = self.matrix.SwapOnVSync(double_buffer)
            time.sleep(0.02)

# Main function
# e.g. call with
#  sudo ./image-scroller.py --chain=4
# if you have a chain of four
if __name__ == "__main__":
    out = "Welcome to ヨォドォバァシィカァメェラ。亲爱的顾客朋友、你们好。衷心欢迎您光临友都八喜。友都­八喜是日本著名的大型购物中心。精明商品将近一百万种、数码相机、摄像机、名牌手表、­化妆品、电子游戏、名牌箱包等应有尽有。最新的款式、最优惠的价格、最优质的服务。"
    subprocess.call('sudo convert -background black -fill "#e8ad35" -font /usr/share/fonts/truetype/jfdot/JF-Dot-jiskan24.ttf -pointsize 30 label:"{0}" /home/pi/rpi-clock/sign.png'.format(out),shell=True)
    subprocess.call('sudo python3 image-scroller.py --led-chain=1 --led-cols=64 -i sign.png -b 80 --led-no-hardware-pulse 1',shell=True)

    image_scroller = ImageScroller()
    if (not image_scroller.process()):
        image_scroller.print_help()
