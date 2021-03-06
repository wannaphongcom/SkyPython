'''
// Copyright 2010 Google Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
// 
// Original Author: Brent Bryan
// 
// Notification of Change: The original java source code has been
// modified in that it has been rewritten in the python programming
// language and additionally, may contain components and ideas that are 
// not found in the original source code.


   Copyright 2013 Neil Borle and Paul Lu

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


Created on 2013-05-22

@author: Neil Borle
'''

from Layer import Layer
from src.renderer.RendererObjectManager import RendererObjectManager
from src.search.SearchResult import SearchResult

class SourceLayer(Layer):
    '''
    An extention of Layer which has additional methods.
    '''
    class SourceUpdateClosure(object):
        '''
        Update closure that allows sources to be
        updated for a given layer.
        '''
        source_layer = None
        
        def run(self):
            self.source_layer.refresh_sources()
        
        def __init__(self, layer):
            '''
            constructor
            '''
            self.source_layer = layer
    
    search_index = {}
    # prefix_store = prefixstore class
    
    def initialize(self):
        self.astro_sources = []
        self.initialize_astro_sources(self.astro_sources)
        
        for astro_source in self.astro_sources:
            source = astro_source.initialize()
            
            self.image_sources += source.get_images()
            self.line_sources += source.get_lines()
            self.point_sources += source.get_points()
            self.text_sources += source.get_labels()
            
            if source.names != []:
                gc_search_loaction = source.get_geo_coords()
                for name in source.names:
                    self.search_index[str(name).lower()] = \
                        SearchResult(name, gc_search_loaction)
                    # prefix_store.add(str(name).lower())
        self.update_layer_for_controller_change()
        
    def update_layer_for_controller_change(self):
        r = RendererObjectManager(0, None)
        self.refresh_sources(set([r.update_type.Reset]))
        if self.should_update:
            if self.closure == None:
                self.closure = self.SourceUpdateClosure(self)
            self.add_update_closure(self.closure)
            
    def refresh_sources(self, update_types=set()): # this needs to be synchronized!
        #for astro_source in self.astro_sources:
        #    update_types = set(update_types + astro_source.update())

        if len(update_types) != 0:
            self.redraw(update_types)
    
    def redraw(self, update_types=set()):
        if len(update_types) == 0:
            r = RendererObjectManager(0, None)
            self.refresh_sources(set([r.update_type.Reset]))
        else:
            Layer.redraw(self, self.point_sources, self.line_sources, \
                         self.text_sources, self.image_sources, update_types)
            
    def search_by_object_name(self):
        raise NotImplementedError("haven't done searching yet")
    
    def get_object_names_matching_prefix(self):
        raise NotImplementedError("haven't done searching yet")
    
    def __init__(self, boolean):
        '''
        Constructor
        '''
        Layer.__init__(self)
        self.closure = None
        self.should_update = boolean
        self.text_sources = []
        self.image_sources = []
        self.point_sources = []
        self.line_sources = []
        self.astro_sources = []