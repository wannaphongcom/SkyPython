'''
Created on 2013-05-24

@author: Neil
'''

class LayerManager(object):
    '''
    classdocs
    '''
    layers = []

    def add_layer(self, layer):
        self.layers.append(layer)
        
    def init_layers(self):
        for layer in self.layers:
            layer.initialize()
            
    def register_with_renderer(self):
        raise NotImplementedError("not implemented")
    
    def on_shared_preference_change(self):
        raise NotImplementedError("not implemented")
    
    def get_string(self):
        return "Layer Manager"
    
    def search_by_object_name(self):
        raise NotImplementedError("not implemented")
    
    def get_object_names_matching_prefix(self):
        raise NotImplementedError("not implemented")
    
    def is_layer_visible(self):
        raise NotImplementedError("not implemented")

    def __init__(self):
        '''
        Constructor
        '''
        