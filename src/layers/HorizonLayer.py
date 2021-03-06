'''
// Copyright 2008 Google Inc.
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
// Original Author: John Taylor, Brent Bryan
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


Created on 2013-06-24

@author: Neil Borle
'''

from time import mktime
from SourceLayer import SourceLayer
from src.source.AbstractAstronomicalSource import AbstractAstronomicalSource
from src.source.LineSource import LineSource
from src.source.TextSource import TextSource
from src.renderer.RendererObjectManager import RendererObjectManager
from src.units.GeocentricCoordinates import GeocentricCoordinates
from src.base.TimeConstants import MILLISECONDS_PER_SECOND

class HorizonLayer(SourceLayer):
    '''
    Identifies Nadir, the Zenith and the cardinal directions
    '''
    class HorizonSource(AbstractAstronomicalSource):
        '''
        Horizon elements extend Astronomical Sources so that they
        can be rendered just as stars, constellations, ect...
        '''
        # The bug in the G1 rendering code in the original java is
        # not present in the python code. Lines and labels are the same color.
        LINE_COLOR = 0x7856B0F5
        LABEL_COLOR = 0x7856B0F5
        UPDATE_FREQ_MS = 1 * MILLISECONDS_PER_SECOND
        
        def update_coords(self):
            self.last_update_time_Ms = mktime(self.model.get_time())
            
            self.zenith.assign(vector3=self.model.get_zenith())
            self.nadir.assign(vector3=self.model.get_nadir())
            self.north.assign(vector3=self.model.get_north())
            self.south.assign(vector3=self.model.get_south())
            self.east.assign(vector3=self.model.get_east())
            self.west.assign(vector3=self.model.get_west())
            
        def initialize(self):
            self.update_coords()
            return self
        
        #override(AbstractAstronomicalSource)
        def update(self):
            update_types = set()
            
            if abs(mktime(self.model.get_time()) - self.last_update_time_Ms > self.UPDATE_FREQ_MS):
                self.update_coords()
                update = RendererObjectManager().update_type.UpdatePositions
                update_types = set([update])
                
            return update_types
        
        #override(AbstractAstronomicalSource)
        def get_labels(self):
            return self.text_sources
        
        #override(AbstractAstronomicalSource)
        def get_lines(self):
            return self.line_sources
        
        def __init__(self, model):
            '''
            constructor
            '''
            AbstractAstronomicalSource.__init__(self)
            self.zenith = GeocentricCoordinates(0, 0, 0)
            self.nadir = GeocentricCoordinates(0, 0, 0)
            self.north = GeocentricCoordinates(0, 0, 0)
            self.south = GeocentricCoordinates(0, 0, 0)
            self.east = GeocentricCoordinates(0, 0, 0)
            self.west = GeocentricCoordinates(0, 0, 0)
        
            self.line_sources = []
            self.text_sources = []
        
            self.lastUpdateTimeMs = 0
            
            self.model = model
            
            vertices = [self.north, self.east, self.south, self.west, self.north]
            self.line_sources.append(LineSource(vertices, self.LINE_COLOR, 1.5))
            
            self.text_sources.append(TextSource("ZENITH", self.LABEL_COLOR, self.zenith))
            self.text_sources.append(TextSource("NADIR", self.LABEL_COLOR, self.nadir))
            self.text_sources.append(TextSource("NORTH", self.LABEL_COLOR, self.north))
            self.text_sources.append(TextSource("SOUTH", self.LABEL_COLOR, self.south))
            self.text_sources.append(TextSource("EAST", self.LABEL_COLOR, self.east))
            self.text_sources.append(TextSource("WEST", self.LABEL_COLOR, self.west))
    
    def initialize_astro_sources(self, sources):
        sources.append(self.HorizonSource(self.model))
    
    def get_layer_id(self):
        return -106
    
    def get_layer_name_id(self):
        raise NotImplementedError("not implemented yet")
    
    def get_preference_id(self):
        return "source_provider.6"
    
    def get_layer_name(self):
        return "Horizon"

    def __init__(self, model):
        '''
        Constructor
        '''
        SourceLayer.__init__(self, True)
        self.model = model
        