'''
Created on Jan 30, 2024

@author: Pat Deegan
@copyright: Copyright (C) 2024 Pat Deegan, https://psychogenic.com
'''

from skip.property.property import ElementWithPropertiesWrapper
from skip.sexp.parser import ParsedValue
from skip.element_template import ElementTemplate
from skip.collection import ElementCollection

class SheetWrapper(ElementWithPropertiesWrapper):
    def __init__(self, pv:ParsedValue):
        super().__init__(pv)

class SheetCollection(ElementCollection):
    def __init__(self, parent, elements:list):
        super().__init__(parent, elements)
        
    def all_at(self, x:float, y:float):
        ret_val = []
        for w in self:
            for p in w.points:
                #print(f"CHECK {p.value} for {x},{y}")
                if p.value[0] == x and p.value[1] == y:
                    ret_val.append(w)
        
        return ret_val
    
    
    def within_circle(self, xcoord:float, ycoord:float, radius:float):
        '''    
            Find all elements of this collection that are within the 
            circle of radius radius, centered on xcoord, ycoord.
            
            @note: only works for elements that have a
            suitable 'at' or 'location' attribute
        
        '''
        retvals = []
        if not len(self._elements):
            return retvals
        
        
        target_coords = [xcoord, ycoord]
        for el in self:
            append = False
            for p in el.points:
                if self._distance_between(target_coords, p.value) <= radius:
                    append = True
                    
            if append:
                retvals.append(el)
            
        return retvals
        
    
    def _new_instance(self):
        newObj = SheetWrapper(self.parent.new_from_list(ElementTemplate['sheet']))
        return newObj
        
    def __repr__(self):
        return f'<SheetCollection ({len(self)} sheets)>'
