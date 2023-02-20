#reference: https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/Ustx/UCurve.cs

from typing import List, Optional
from .UExpression import UExpressionDescriptor

class UCurve:
    interval:int = 5
    xs:List[int] = []
    ys:List[int] = []
    abbr:str = ""
    descriptor:UExpressionDescriptor = None

    def __init__(self, 
            descriptor:Optional[UExpressionDescriptor] = None,
            abbr:Optional[str]=None
        ):
        if descriptor is not None:
            self.descriptor = descriptor
            self.abbr = descriptor.abbr
            return
        this.abbr = abbr
    
    def to_dict(self):
        return {
            "interval": self.interval,
            "xs": self.xs,
            "ys": self.ys,
            "abbr": self.abbr,
        }   
    
    @classmethod
    def from_dict(cls, d):
        obj = cls(d["abbr"])
        obj.interval = d["interval"]
        obj.xs = d["xs"]
        obj.ys = d["ys"]
        return obj
    