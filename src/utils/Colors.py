'''
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


Created on 2013-05-20

@author: Neil Borle
'''

from Enumeration import enum

'''
Create a colour enum for easy access to the
hex values for all of the following colours
'''
colors = enum(\
WHITE=0xFFFFFF, \
IVORY=0xFFFFF0, \
LIGHTYELLOW=0xFFFFE0, \
YELLOW=0xFFFF00, \
SNOW=0xFFFAFA, \
FLORALWHITE=0xFFFAF0, \
LEMONCHIFFON=0xFFFACD, \
CORNSILK=0xFFF8DC, \
SEASHELL=0xFFF5EE, \
LAVENDERBLUSH=0xFFF0F5, \
PAPAYAWHIP=0xFFEFD5, \
BLANCHEDALMOND=0xFFEBCD, \
MISTYROSE=0xFFE4E1, \
BISQUE=0xFFE4C4, \
MOCCASIN=0xFFE4B5, \
NAVAJOWHITE=0xFFDEAD, \
PEACHPUFF=0xFFDAB9, \
GOLD=0xFFD700, \
PINK=0xFFC0CB, \
LIGHTPINK=0xFFB6C1, \
ORANGE=0xFFA500, \
LIGHTSALMON=0xFFA07A, \
DARKORANGE=0xFF8C00, \
CORAL=0xFF7F50, \
HOTPINK=0xFF69B4, \
TOMATO=0xFF6347, \
ORANGERED=0xFF4500, \
DEEPPINK=0xFF1493, \
FUCHSIA=0xFF00FF, \
MAGENTA=0xFF00FF, \
RED=0xFF0000, \
OLDLACE=0xFDF5E6, \
LIGHTGOLDENRODYELLOW=0xFAFAD2, \
LINEN=0xFAF0E6, \
ANTIQUEWHITE=0xFAEBD7, \
SALMON=0xFA8072, \
GHOSTWHITE=0xF8F8FF, \
MINTCREAM=0xF5FFFA, \
WHITESMOKE=0xF5F5F5, \
BEIGE=0xF5F5DC, \
WHEAT=0xF5DEB3, \
SANDYBROWN=0xF4A460, \
AZURE=0xF0FFFF, \
HONEYDEW=0xF0FFF0, \
ALICEBLUE=0xF0F8FF, \
KHAKI=0xF0E68C, \
LIGHTCORAL=0xF08080, \
PALEGOLDENROD=0xEEE8AA, \
VIOLET=0xEE82EE, \
DARKSALMON=0xE9967A, \
LAVENDER=0xE6E6FA, \
LIGHTCYAN=0xE0FFFF, \
BURLYWOOD=0xDEB887, \
PLUM=0xDDA0DD, \
GAINSBORO=0xDCDCDC, \
CRIMSON=0xDC143C, \
PALEVIOLETRED=0xDB7093, \
GOLDENROD=0xDAA520, \
ORCHID=0xDA70D6, \
THISTLE=0xD8BFD8, \
LIGHTGREY=0xD3D3D3, \
TAN=0xD2B48C, \
CHOCOLATE=0xD2691E, \
PERU=0xCD853F, \
INDIANRED=0xCD5C5C, \
MEDIUMVIOLETRED=0xC71585, \
SILVER=0xC0C0C0, \
DARKKHAKI=0xBDB76B, \
ROSYBROWN=0xBC8F8F, \
MEDIUMORCHID=0xBA55D3, \
DARKGOLDENROD=0xB8860B, \
FIREBRICK=0xB22222, \
POWDERBLUE=0xB0E0E6, \
LIGHTSTEELBLUE=0xB0C4DE, \
PALETURQUOISE=0xAFEEEE, \
GREENYELLOW=0xADFF2F, \
LIGHTBLUE=0xADD8E6, \
DARKGRAY=0xA9A9A9, \
BROWN=0xA52A2A, \
SIENNA=0xA0522D, \
YELLOWGREEN=0x9ACD32, \
DARKORCHID=0x9932CC, \
PALEGREEN=0x98FB98, \
DARKVIOLET=0x9400D3, \
MEDIUMPURPLE=0x9370DB, \
LIGHTGREEN=0x90EE90, \
DARKSEAGREEN=0x8FBC8F, \
SADDLEBROWN=0x8B4513, \
DARKMAGENTA=0x8B008B, \
DARKRED=0x8B0000, \
BLUEVIOLET=0x8A2BE2, \
LIGHTSKYBLUE=0x87CEFA, \
SKYBLUE=0x87CEEB, \
GRAY=0x808080, \
OLIVE=0x808000, \
PURPLE=0x800080, \
MAROON=0x800000, \
AQUAMARINE=0x7FFFD4, \
CHARTREUSE=0x7FFF00, \
LAWNGREEN=0x7CFC00, \
MEDIUMSLATEBLUE=0x7B68EE, \
LIGHTSLATEGRAY=0x778899, \
SLATEGRAY=0x708090, \
OLIVEDRAB=0x6B8E23, \
SLATEBLUE=0x6A5ACD, \
DIMGRAY=0x696969, \
MEDIUMAQUAMARINE=0x66CDAA, \
CORNFLOWERBLUE=0x6495ED, \
CADETBLUE=0x5F9EA0, \
DARKOLIVEGREEN=0x556B2F, \
INDIGO=0x4B0082, \
MEDIUMTURQUOISE=0x48D1CC, \
DARKSLATEBLUE=0x483D8B, \
STEELBLUE=0x4682B4, \
ROYALBLUE=0x4169E1, \
TURQUOISE=0x40E0D0, \
MEDIUMSEAGREEN=0x3CB371, \
LIMEGREEN=0x32CD32, \
DARKSLATEGRAY=0x2F4F4F, \
SEAGREEN=0x2E8B57, \
FORESTGREEN=0x228B22, \
LIGHTSEAGREEN=0x20B2AA, \
DODGERBLUE=0x1E90FF, \
MIDNIGHTBLUE=0x191970, \
AQUA=0x00FFFF, \
CYAN=0x00FFFF, \
SPRINGGREEN=0x00FF7F, \
LIME=0x00FF00, \
MEDIUMSPRINGGREEN=0x00FA9A, \
DARKTURQUOISE=0x00CED1, \
DEEPSKYBLUE=0x00BFFF, \
DARKCYAN=0x008B8B, \
TEAL=0x008080, \
GREEN=0x008000, \
DARKGREEN=0x006400, \
BLUE=0x0000FF, \
MEDIUMBLUE=0x0000CD, \
DARKBLUE=0x00008B, \
NAVY=0x000080, \
BLACK=0x000000)

if __name__ == "__main__":
    '''
    For debugging purposes
    '''
    print colors.NAVY