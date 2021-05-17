svgclip
=======

Sometimes you have an SVG file and you want to reduce its size to the
actual drawing.  I had a hard time finding a good way to do this
programmatically, so I wrote this program back in 2013.

**This is now possible to do only with the help of inkscape itself,** 
according to issue submitter wz1765:

```
inkscape --export-type=svg -o --export-area-drawing ./test.svg
```

There is therefore little need for this program.

Another alternative is [vpype](https://github.com/abey79/vpype).

## Original README contents

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
