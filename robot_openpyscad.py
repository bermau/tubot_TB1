"""Une carcasse de robot"""

# Note : I use a slightly modified version of openpyscad (see my GitHub repo)

# Je veux créer une représentation simple de robot X, Y, Z
# réalisé avec des V-slot 2020

import sys

from local_conf import REP_OF_MY_OPENPYSCAD            # IMPORTANT see my version in bermau/openpyscad

sys.path.append(REP_OF_MY_OPENPYSCAD)
import openpyscad
from openpyscad import Cylinder, Cube, Union

from openpyscad import *

eps = 0.01
X_LONG = 800
Y_LONG = 400
Z_LONG = 300

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


def bar_2020(l, name=None):
    """Very symple representation of V-Slot"""
    print(f"barre : 20x20 x {l} mm {name}")
    return Cube([l, 20, 20])

# delrin mini
solid_mini_wheel_radius = 15.23 / 2
solid_mini_wheel_height = 8.8 
def mini_wheel_OLD():
    return Cylinder(r=solid_mini_wheel_radius, h=solid_mini_wheel_height)

class MiniWheel:
    solid_mini_wheel_radius = 15.23 / 2
    solid_mini_wheel_height = 8.8
    def __init__(self):
        self.struct = Cylinder(r=solid_mini_wheel_radius, h=solid_mini_wheel_height)

# plateau A

# Chariot moyen type : https://fr.aliexpress.com/item/4000177052618.html
chariot_medium = Cube ([65.5, 65.5, 3])
plateau = Cube([100, 80, 3])

def centrer_x(truc):
    return truc.translate([-truc.size[0]/2, 0, 0])

def centrer_y(truc):
    return truc.translate([0, -truc.size[1]/2, 0])

def centrer_z(truc):
    return truc.translate(0, 0, -truc.size[2]/2)

def center(obj, x= True, y=True, z=True):
    """Center an object along its x, y, z axes"""
    return obj.translate([-obj.size[0]/2 * x, -obj.size[1]/2 * y, -obj.size[2]/2 * z])

def mini_slider_pour_20():
    # Petit chariot de type : https://fr.aliexpress.com/item/4000177052618.html
    chariot_mini = Cube([50, 50, 6.5]);
    u = Union()
    wheel = MiniWheel().struct
    # wheel = delrin.struct
    # ecart_x, ecart_y : ecart entre les axes des roues
    ecart_y = 20 + MiniWheel.solid_mini_wheel_radius * 2
    ecart_x = 20 + MiniWheel.solid_mini_wheel_radius * 2 + 20
    u.append(chariot_mini.translate([0, 0, 20]))

    wheel_group = Union()
    wheel_group.append(wheel)
    wheel_group.append(wheel.translate([ecart_x, 0, 0]))
    wheel_group.append(wheel.translate([ecart_x, ecart_y, 0]))
    wheel_group.append(wheel.translate([ 0, ecart_y, 0]))

    x_dec = (plateau.size[0] - ecart_x) / 2
    y_dec = (plateau.size[1] - ecart_y) / 2
    z_dec = (20 - solid_mini_wheel_height)/2
    u.append(wheel_group.translate([x_dec, y_dec, z_dec]))

    return u.translate([-plateau.size[0]/2,-plateau.size[1]/2,  -20])

def carcasse():
    u = Union()
    bar_x = bar_2020(X_LONG, "barre x")
    Z_DEC = Z_LONG - 20

    u.append(bar_x)
    u.append(bar_x.translate([0, 0, Z_DEC]))
    u.append(bar_x.translate([0, Y_LONG-20, Z_DEC]))
    u.append(bar_x.translate([0, Y_LONG-20, 0]))

    bar_y = bar_2020(Y_LONG-40, "barre y").rotate([0, 0, 90]).translate([20, 20, 0]).color('Orange')
    u.append(bar_y).translate([0, 0, Z_DEC])
    u.append(bar_y.translate([0, 0, Z_DEC]))
    u.append(bar_y.translate([X_LONG-20, 0, 0]))
    u.append(bar_y.translate([X_LONG - 20, 0, Z_DEC]))
    # u.append(bar_y.translate([0,Y_LONG,0]))
    bar_z = bar_2020(Z_LONG-40, "barre Z").rotate([0, -90, 0]).translate([20, 0, 20]).color('Chartreuse')

    u.append(bar_z)
    u.append(bar_z.translate([X_LONG-20, 0, 0]))
    u.append(bar_z.translate([X_LONG-20, Y_LONG-20, 0]))
    u.append(bar_z.translate([0, Y_LONG - 20, 0]))
    return u

def axis_y_on_2_sliders():
    u = Union()
    u += mini_slider_pour_20().color('DarkOrange').translate([Nonevaluated("position($t)"), 10, Z_LONG]).post_comment("Y slider 1")
    u += mini_slider_pour_20().color('DarkOrange').translate([Nonevaluated("position($t)"), Y_LONG - 10, Z_LONG]).post_comment("Y slider 2")
    u += bar_2020(Y_LONG + 100, "chariot y").rotate([0, 0, 90]).color('Purple', 0.5).translate([10,0,0]).translate([Nonevaluated("position($t)"), -30, Z_LONG]).post_comment("Y axis")
    return u

def axis_y_sup():
    """Partie mobile se déplacant le long de l'axe Y, en haut. """
    u = Union()
    u += mini_slider_pour_20().rotate([0,0,90]).color('LightBlue', 0.8).translate([Nonevaluated("position($t)"), 10, Z_LONG+ 20]).post_comment("slider 1")
    return u.translate([-10 ,Nonevaluated("pos_y_sup($t)"), plateau.size[2]])

if __name__ == '__main__':

    output_file = __file__.replace('.py', '.scad')

    # below : Noneval()
    (
            carcasse().post_comment("End of CARCASSE")
            + axis_y_on_2_sliders().post_comment("End of AXIS_Y + 2 sliders")
            + axis_y_sup().post_comment("End of AXIS_Y_SUP")
     ).write(output_file, prologue=scad_str)
    print("Open result with OpenSCAD", output_file)
    # mini_slider_pour_20().color('blue').write("robot.scad")
    # (mini_slider_pour_20()).write(output_file)