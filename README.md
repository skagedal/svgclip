
svgclip (updated)
=======

I found this package today and after some trial and error was able to get this script to clip an svg image. Since it looks like this is no longer maintained I thought I'd document how I got this to work in Ubuntu 19.04. 

I am not a python developer and I am not positive which of these items I installed were needed or not. Here's what I installed:

```bash
sudo apt install python-pip
sudo apt-get install inkscape python-rsvg python-cairo # from the documentation. python-rsvg doesn't seem to exist anymore though so,
sudo apt-get install inkscape python-cairo # I think this didn't install the write package
sudo apt-get install librsvg2-bin # may or may not be necessary?
sudo apt install libcanberra-gtk-module libcanberra-gtk3-module # may or may not be necessary?
sudo apt-get install python-gi-cairo # I'm pretty sure this is what got python cairo to work
```

I had to modify the script after some errors were produced after I finally got the right packages installed. See script for more details. 
   
   
   
   
   
   
---
ORIGINAL README BELOW
---

svgclip
=======

Sometimes you have an SVG file and you want to reduce its size to the
actual drawing.  I have had a hard time finding a good way to do this
programmatically, for batch processing or other.

Googling around, one method I've found is to use Inkscape. It can be
scripted like this:

    inkscape --verb=FitCanvasToDrawing --verb=FileSave --verb=FileClose *.svg

That takes a long time, opens up a GUI and isn't very flexible.

However, you can also get information about the bounding box with the 
`--query-all` option to inkscape. Using this information, I wrote a python
script that uses rsvg and cairo to write the drawing to a file with the 
right dimensions.

Since it was easy, I also added an option to add a margin to the drawing.

Make sure you have Inkscape, python-rsvg and python-cairo installed
(on Ubuntu, try `sudo apt-get install inkscape python-rsvg python-cairo`)
and then run `svgclip.py inputfile -o outputfile [-m marginpixels]`.

Regards,
Simon Kågedal Reimer
