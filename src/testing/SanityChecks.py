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
// Notification of Change: The original java source code has been heavily
// modified in that it has been rewritten in the python programming
// language and additionaly may component and ideas not found in the 
// original source code.
'''

'''
Created on 2013-07-26

@author: Alyson Wu and Morgan Redshaw
'''

# Equivalent of the Java programs EqualsTester

class smallClass:
    value = 0
    
    def equals(self, other):
        return self.value == other.value
    
def EqualsTester():
    '''
    >>> groups = [[smallClass for i in range(5)] for x in range(3)]
    
    # Test equals
    >>> allCorrect = True
    
    >>> for group in groups:
    ...    for obj1 in group:
    ...        allCorrect = (obj1 == obj1) & allCorrect
    ...        
    ...        for obj2 in group:
    ...            if obj1 != obj2:
    ...                allCorrect = obj1.equals(obj2) & allCorrect
    
    >>> allCorrect
    True
    
    >>> allCorrect = True
    
    >>> for group1 in groups:
    ...    for group2 in groups:
    ...        if group1 != group2:
    ...            for obj1 in group1:
    ...                for obj2 in group2:
    ...                    allCorrect = (not obj1.equals(obj2)) & allCorrect
    
    >>> allCorrect
    True
    '''
    pass