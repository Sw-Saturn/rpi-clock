#!/usr/bin/env python3
# coding: UTF-8
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
from datetime import datetime
import time
from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
 
class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="21:52")
 
    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font_time = graphics.Font()
        #font.LoadFont("../../../fonts/mplus_h12r.bdf")
        font_time.LoadFont("./fonts/21-Adobe-Helvetica.bdf")
        #font.LoadFont("../../../fonts/15-Adobe-Helvetica.bdf")
        font.LoadFont("./fonts/16-Adobe-Helvetica-Bold.bdf")

        textColor = graphics.Color(245, 0, 111)
        timeColor = graphics.Color(61, 147, 215)
        pos = offscreen_canvas.width
        my_text = self.args.text
        
        while True:
            d = datetime.now()
            h = (" " + str(d.hour))[-2:]
            #スペースを頭に着けて最後から2文字背取得。1-9時の間も真ん中に時計が表示されるようにする考慮
            #date_text = d.strftime("%a %b %d %Y")
            date_text = d.strftime("%a %m.%d")
            time_text = d.strftime("%H:%M")
            #logger.debug(my_text) 
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, 0, 14, textColor, date_text)
            len1 = graphics.DrawText(offscreen_canvas, font_time,7, 30, timeColor, time_text)
 
            #time.sleep(60)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            #time.sleep(60)
 
# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
