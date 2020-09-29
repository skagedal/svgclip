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

## Requirements

`apt-get install inkscape gir1.2-rsvg-2.0 python-gi-cairo`

## Usage

`svgclip.py inputfile -o outputfile [-m marginpixels]`

Regards,
Simon Kågedal Reimer
