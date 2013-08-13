'''
Created on 2013-06-17

@author: Neil
'''

import threading
import calendar
from src.base.TimeConstants import MILLISECONDS_PER_MINUTE
from src.provider.SolarPositionCalculator import get_solar_position
from src.units.GeocentricCoordinates import get_instance

class SkyGradientLayer(object):
    '''
    classdocs
    '''
    renderer_lock = threading.RLock()
    UPDATE_FREQUENCY_MS = 5 * MILLISECONDS_PER_MINUTE
    
    def initialize(self):
        # Do Nothing
        pass
    
    def register_with_renderer(self, rend_controller):
        self.controller = rend_controller
        self.redraw()
    
    def set_visible(self, visible):
        if visible:
            self.redraw()
        else:
            with self.renderer_lock:
                self.controller.queue_disable_sky_gradient()
    
    def redraw(self):
        model_time = self.model.get_time()
        Ms_since_epoch = calendar.timegm(model_time) * 100
        
        if abs(Ms_since_epoch - self.last_update_time_Ms) > self.UPDATE_FREQUENCY_MS:
            self.last_update_time_Ms = Ms_since_epoch
            
            sun_pos = get_solar_position(model_time)
            
            with self.renderer_lock:
                gc = get_instance(sun_pos.ra, sun_pos.dec)
                self.controller.queue_enable_sky_gradient(gc)
    
    def get_layer_id(self):
        return 0
    
    def get_layer_name(self):
        return "Sky Gradient"
    
    def get_preference_id(self):
        return "source_provider.8"
    
    def get_layer_name_id(self):
        raise NotImplementedError("not implemented yet")
    
    def search_by_object_name(self, name):
        return []
    
    def get_object_names_matching_prefix(self, prefix):
        return set()


    def __init__(self, model):
        '''
        Constructor
        '''
        self.model = model
        self.controller = None
        self.last_update_time_Ms = 0
        
        
        