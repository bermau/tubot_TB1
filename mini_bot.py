"""Une mini carcasse de robot"""

# Note : I use a slightly modified version of openpyscad (see my GitHub repo)

# Je veux créer une représentation simple de robot X, Y, Z
# réalisé avec des V-slot 2020

import sys

from local_conf import REP_OF_MY_OPENPYSCAD            # IMPORTANT see my version in bermau/openpyscad

sys.path.append(REP_OF_MY_OPENPYSCAD)
import openpyscad
from openpyscad import Cylinder, Cube, Union

from openpyscad import *


# from solid import scad_render_animated_file
# from solid.objects import square, translate
# from solid.solidpython import OpenSCADObject

eps = 0.01
# Dimensions pour tenir dans un caisson de type Ikea
X_LONG = 330
Y_LONG = 400 - 40 - 60
Z_LONG = 330 - 80
solid_wheel_radius = 12
solid_wheel_height = 11

# Représentation, déplacements
plate_x_offset = X_LONG - 114
plate_y_offset = 250

scad_str = """
// time varies fro 0 to 1 and 1 to 0
function position(time) = time < 0.5
      ? {var1} + (time * {var2})
      : {var1} + ({var2}/2 - ((time-0.5) * {var2})) ;

""".format(var1="50", var2=str(plate_x_offset*2))
scad_str += """

function pos_y_sup(time) = time < 0.5
      ? {var1} + (time * {var2})
      : {var1} + ({var2}/2 - ((time-0.5) * {var2})) ;
""".format(var1="60", var2=str(plate_y_offset*2))


def bar_2020(l):
    """Very symple representation of V-Slot"""
    print(f"barre : 20x20 x {l} mm")
    return Cube([l, 20, 20])


def solid_wheel():
    return Cylinder(r=solid_wheel_radius, h=solid_wheel_height)

plateau = Cube([100, 80, 3])

def centrer_x(truc):
    return truc.translate([-truc.size[0]/2, 0, 0])

def center(obj, x= True, y=True, z=True):
    """Center an object along its x, y, z axes"""
    return obj.translate([-obj.size[0]/2 * x, -obj.size[1]/2 * y, -obj.size[2]/2 * z])

def slider_pour_20():
    u = Union()
    wheel = solid_wheel()
    # ecart_x, ecart_y : ecart entre les axes des roues
    ecart_y = 20 + solid_wheel_radius*2
    ecart_x = 20 + solid_wheel_radius*2 + 20
    u.append(plateau.translate([0, 0, 20]))

    wheel_group = Union()
    wheel_group.append(wheel)
    wheel_group.append(wheel.translate([ecart_x, 0, 0]))
    wheel_group.append(wheel.translate([ecart_x, ecart_y, 0]))
    wheel_group.append(wheel.translate([ 0, ecart_y, 0]))

    x_dec = (plateau.size[0] - ecart_x) / 2
    y_dec = (plateau.size[1] - ecart_y) / 2
    z_dec = (20 - solid_wheel_height)/2
    u.append(wheel_group.translate([x_dec, y_dec, z_dec]))

    return u.translate([-plateau.size[0]/2,-plateau.size[1]/2,  -20])

def carcasse():
    u = Union()
    bar_x = bar_2020(X_LONG)
    Z_DEC = Z_LONG - 20

    u.append(bar_x)
    u.append(bar_x.translate([0, 0, Z_DEC]))
    u.append(bar_x.translate([0, Y_LONG-20, Z_DEC]))
    u.append(bar_x.translate([0, Y_LONG-20, 0]))

    bar_y = bar_2020(Y_LONG-40).rotate([0, 0, 90]).translate([20, 20, 0]).color('Orange')
    u.append(bar_y).translate([0, 0, Z_DEC])
    u.append(bar_y.translate([0, 0, Z_DEC]))
    u.append(bar_y.translate([X_LONG-20, 0, 0]))
    u.append(bar_y.translate([X_LONG - 20, 0, Z_DEC]))
    # u.append(bar_y.translate([0,Y_LONG,0]))
    bar_z = bar_2020(Z_LONG-40).rotate([0, -90, 0]).translate([20, 0, 20]).color('Chartreuse')

    u.append(bar_z)
    u.append(bar_z.translate([X_LONG-20, 0, 0]))
    u.append(bar_z.translate([X_LONG-20, Y_LONG-20, 0]))
    u.append(bar_z.translate([0, Y_LONG - 20, 0]))
    return u

def axis_y():
    u = Union()
    u += slider_pour_20().color('DarkOrange').translate([Nonevaluated("position($t)"), 10, Z_LONG]).comment("Y slider 1")
    u += slider_pour_20().color('DarkOrange').translate([Nonevaluated("position($t)"), Y_LONG - 10, Z_LONG]).comment("Y slider 2")
    u += bar_2020(Y_LONG + 60).rotate([0, 0, 90]).color('Purple', 0.5).translate([10,0,0]).translate([Nonevaluated("position($t)"), -30, Z_LONG]).comment("Y axis")
    return u

def axis_y_sup():
    """Partie mobile se déplacant le long de l'axe Y, en haut. """
    u = Union()
    u += slider_pour_20().rotate([0,0,90]).color('LightBlue', 0.8).translate([Nonevaluated("position($t)"), 10, Z_LONG+ 20]).comment("slider 1")
    return u.translate([-10 ,Nonevaluated("pos_y_sup($t)"), plateau.size[2]])

if __name__ == '__main__':

    output_file = __file__.replace('.py', '.scad')

    # below : Noneval()
    (
    carcasse().comment("End of CARCASSE")
    + axis_y().comment("End of AXIS_Y")
    + axis_y_sup().comment("End of AXIS_Y_SUP")
     ).write(output_file, prologue=scad_str)
    print("Open result with OpenSCAD", output_file)
    # slider_pour_20().color('blue').write("robot.scad")
    # (slider_pour_20()).write(output_file)