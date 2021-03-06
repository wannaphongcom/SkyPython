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


Created on 2013-05-16

@author: Neil Borle
'''

from PySide.QtGui import QPixmap
from Source import Source
from src.units.Vector3 import Vector3
from src.utils.Colors import colors
from src.utils.VectorUtil import negate, normalized, cross_product

class ImageSource(Source):
    '''
    A celestial object represented by an image, such as a planet or a galaxy.
    
    // These two vectors, along with Source.xyz, determine the position of the
    // image object.  The corners are as follows
    //
    //  xyz-u+v   xyz+u+v
    //     +---------+     ^
    //     |   xyz   |     | v
    //     |    .    |     .
    //     |         |
    //     +---------+
    //  xyz-u-v    xyz+u-v
    //
    //          .--->
    //            u
    '''
    image_scale = 1

    def get_horizontal_corner(self):
        return [self.ux, self.uy, self.uz]
    
    def get_verical_corner(self):
        return [self.vx, self.vy, self.vz]
    
    def set_up_vector(self, up_v):
        p = self.geocentric_coords
        u = negate(normalized(cross_product(p, up_v)))
        v = cross_product(u, p)
        v.scale(self.image_scale)
        u.scale(self.image_scale)
        
        self.ux = u.x
        self.uy = u.y
        self.uz = u.z
        
        self.vx = v.x
        self.vy = v.y
        self.vz = v.z
    
    def set_image_id(self, input_id):
        # hack bool to prevent blank meteors from rendering
        self.is_blank = True if input_id == 'blank' else False
        
        url = "assets/drawable/" + input_id + ".png"
        self.pixmap_image = QPixmap()
        
        if not self.pixmap_image.load(url):
            raise RuntimeError("Could not load image resource")
    
    def __init__(self, geo_coord, new_id, up_v=Vector3(0.0, 1.0, 0.0), im_scale=1):
        '''
        Constructor
        '''
        Source.__init__(self, colors.WHITE, geo_coord)
        self.is_blank = False
        self.requires_blending = False
        self.pixmap_image = None
        self.image_scale = im_scale
        self.set_up_vector(up_v)
        self.set_image_id(new_id)
        
    