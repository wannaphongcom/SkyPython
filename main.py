'''
Created on 2013-05-14

@author: Neil
'''

import sys
from PySide.QtGui import QApplication

from skypython.SkyPython import SkyPython
from layers.LayerManager import LayerManager
from layers.LayerManager import instantiate_layer_manager
from source.AstronomicalSource import AstronomicalSource
from control.AstronomerModel import AstronomerModel
from renderer.PointObjectManager import PointObjectManager
from renderer.SkyRenderer import SkyRenderer
from control.ZeroMagneticDeclinationCalculator import ZeroMagneticDeclinationCalculator as ZMDC

def start_application():
    layer_manager = instantiate_layer_manager()
    layer_manager.init_layers()
    model = AstronomerModel(ZMDC())
    POM = PointObjectManager(-100, None)
    
    points = []
    for proto_source in layer_manager.layers[0].astro_sources:
        new_astro = AstronomicalSource()
        new_astro.names = proto_source.names
        new_astro.geocentric_coords = proto_source.get_geo_coords()
        new_astro.image_sources = proto_source.get_images()
        new_astro.point_sources = proto_source.get_points()
        new_astro.line_sources = proto_source.get_lines()
        new_astro.text_sources = proto_source.get_labels()
        points += new_astro.point_sources
    POM.update_objects(points, None)
    
    sky_renderer = SkyRenderer()
    sky_renderer.add_object_manager(POM)
    
    app = QApplication(sys.argv)
    w = SkyPython(sky_renderer)
    w.show()
    app.exec_()

if __name__ == '__main__':
    start_application()
    
    