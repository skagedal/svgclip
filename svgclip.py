#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
svgclip.py

Copyright (c) 2013 Simon Kågedal Reimer

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

import argparse
import subprocess
import cairo
from gi.repository import Rsvg

def query_svg(svgfile):
    """Parses the output from inkscape --query-all"""
    def parse_line(line):
        split = line.split(b',')
        return [split[0]] + [float(x) for x in split[1:]]
    output = subprocess.check_output(["inkscape", "--query-all", svgfile])
    lines = output.split(b'\n')
    return [parse_line(line) for line in lines]

def get_bounding_box(svgfile):
    all = query_svg(svgfile)
    # The first line seems to always be the full drawing
    return all[0]

def print_info(svgfile):
    bbox = get_bounding_box(svgfile)
    print("""
X:      %f
Y:      %f
Width:  %f
Height: %f""".strip() % tuple(bbox[1:]))

def clip(inputfile, outputfile, margin):
    name, x, y, width, height = get_bounding_box(inputfile)
    
    handle = Rsvg.Handle()
    svg = handle.new_from_file(inputfile)
    surface = cairo.SVGSurface(outputfile, 
                               width + margin * 2, 
                               height + margin * 2)
    ctx = cairo.Context(surface)
    ctx.translate(-x + margin, -y + margin)
    svg.render_cairo(ctx)
    surface.finish()

def arg_parser():
    parser = argparse.ArgumentParser(description=
                                     'Clip SVG file to bounding box.')
    parser.add_argument('input', 
                        help="SVG file to read")
    parser.add_argument('-o', '--output',
                        help="SVG file to write",
                        metavar="SVGFILE")
    parser.add_argument('-m', '--margin',
                        help="Margin to add",
                        metavar="PIXELS",
                        default=0,
                        type=float)
    return parser

if __name__ == "__main__":
    args = arg_parser().parse_args()
    if args.output is None:
        print_info(args.input)
    else:
        clip(args.input, args.output, args.margin)
