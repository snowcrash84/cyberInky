CyberInky Code by Roman Mironov


from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from datetime import *

#Calculate release date
today = date.today()
release_date = date(2020,9,17)
diff = release_date - today

#Configure InkyPHAT
inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.BLACK)

# Load graphic
img = Image.open("/home/pi/Downloads/cyberInky/cyberpunk_red3.png")

#Print text
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("/home/pi/Downloads/cyberInky/hacker.otf", 18)

message= ">Days left: "+str(diff.days)
w, h = font.getsize(message)
x = 10
y = 80

draw.text((x, y), message, inky_display.WHITE, font)
inky_display.set_image(img)
inky_display.show()
