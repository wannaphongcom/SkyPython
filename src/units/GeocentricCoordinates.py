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
// Original Author: Brent Bryan
// 
// Notification of Change: The original java source code has been heavily
// modified in that it has been rewritten in the python programming
// language and additionaly may component and ideas not found in the 
// original source code.
'''

'''
Created on 2013-05-16

@author: Neil Borle
'''

import math
from Vector3 import Vector3

def get_instance(ra, dec):
    coords = GeocentricCoordinates(0.0, 0.0, 0.0)
    coords.update_from_ra_dec(ra, dec)
    return coords

def get_instance_from_list(l):
    return GeocentricCoordinates(l[0], l[1], l[2])

def get_instance_from_vector3(v3):
    return GeocentricCoordinates(v3.x, v3.y, v3.z)

class GeocentricCoordinates(Vector3):
    '''
    classdocs
    '''

    def update_from_ra_dec(self, ra, dec):
        ra_radians = ra * (math.pi / 180.0)
        dec_radians = dec * (math.pi / 180.0)
        
        self.x = math.cos(ra_radians) * math.cos(dec_radians)
        self.y = math.sin(ra_radians) * math.cos(dec_radians)
        self.z = math.sin(dec_radians)
    
    def update_from_list(self, l):
        self.x = l[0]
        self.y = l[1]
        self.z = l[2]
        
    def copy(self):
        return GeocentricCoordinates(self.x, self.y, self.z)

    def __init__(self, new_x, new_y, new_z):
        '''
        Constructor
        '''
        Vector3.__init__(self, new_x, new_y, new_z)
        
if __name__ == "__main__":
    '''
    For debugging purposes
    ready for testing
    '''
    GC = GeocentricCoordinates(4.0, 5.0, 0.0)
    print GC.x, GC.y, GC.z
    GC.assign(vector3=Vector3(1.0, 3.0, 5.0))
    print GC.to_float_array()
    