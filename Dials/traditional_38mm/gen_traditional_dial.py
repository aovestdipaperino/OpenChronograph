
'''
gen_traditional_dial.py

sudo apt-get install font-manager
'''
import svgwrite
from svgwrite import cm, mm
import sys
import os

dial_util_path= os.path.dirname(os.path.abspath(__file__)) + "/../tools/"
sys.path.append(dial_util_path)
from dial_util import *


def dial(fname, od=36.7, lw_minor=0.1524, lw_major=0.25,
         upper_color='black', lower_color='white',
         size=('40mm', '40mm'), viewBox=('-20 -20 40 40')):
    
    dwg = svgwrite.Drawing(filename=fname, size=size, viewBox=viewBox, debug=True)
    elems = dwg.add(dwg.g(id='elems', stroke=upper_color, stroke_width=lw_minor))


    dial_args = {
        'cx': 0,
        'cy': 0,
        'r': od / 2,
        'theta_start' : -pi/2,
        'theta_end' : -pi/2 + 2*pi,
        'outline_lw': lw_major,
        'major_inc' : 2*pi/12,    'major_lw' : lw_major*2,    'major_len' : od/25.0,
        'med_inc' : 2*pi/1,        'med_lw' : lw_minor,      'med_len' : od/35.0,
        'minor_inc' : 2*pi/60,   'minor_lw' : lw_minor,    'minor_len' : od/25.0,
        'fill_color' : 'white',
        'major_labels' : ['12','1','2','3','4','5','','7','8','9','10','11'],
        'font_style' : "font-size:4px; font-family:GFS Artemisia; font-weight:bold",
        'text_r_multiplier' : 0.8,
        'text_offset' : (0, 1.5)}
    draw_dial(dwg, elems, **dial_args)

    # Inner ring
    points = arc(0, 0, od/2*0.95, 0, pi*2, 100)
    elems.add(dwg.polyline(points, stroke_width=lw_minor, fill='white', stroke='black')) 

    
    subdial_args = {
        'cx': 0, 'cy': 10, 'r': od / 7.0,
        'theta_start' : -pi/2, 'theta_end' : -pi/2 + 2*pi,
        'outline_lw': lw_minor,
        'major_inc' : 2*pi/12, 'major_lw' : lw_major, 'major_len' : od/35.0,
        'minor_inc' : 2*pi/60,   'minor_lw' : lw_minor,    'minor_len' : od/70.0,
        'fill_color' : 'white',
        'major_labels' : ['60','','10','','20','','30','','40','','50'],
        'font_style' : "font-size:1.0px; font-family:GFS Artemisia; font-weight:bold",
        'text_r_multiplier' : 0.65,
        'text_offset' : (0, 0.3)}
    draw_dial(dwg, elems, **subdial_args)

    dwg.save()


if __name__ == '__main__':
    dial('traditional_copper.svg', od=36.7, lw_minor=0.1524, lw_major=0.25,
         upper_color='black', lower_color='black')

    dial('traditional_soldermask.svg', od=36.7, lw_minor=0.1524*2, lw_major=0.25*2,
         upper_color='black', lower_color='black')
