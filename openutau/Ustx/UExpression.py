#reference: https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/Ustx/UExpression.cs
from enum import Enum
from typing import List, Optional

class UExpressionType(Enum):
    Numerical = "Numerical"
    Options = "Options"
    Curve = "Curve"

class UExpressionDescriptor:
    name:str = ""
    abbr:str = ""
    type:UExpressionType = UExpressionType.Numerical
    minValue:int = 0
    maxValue:int = 100
    defaultValue:int = 50
    isFlags:bool = False
    flag:str= "" 
    options:Optional[List[str]] = None

    def to_dict(self):
        return {
            "name": self.name,
            "abbr": self.abbr,
            "type": self.type.value,
            "minValue": self.minValue,
            "maxValue": self.maxValue,
            "default_value": self.defaultValue,
            "is_flags": self.isFlags,
            "flag": self.flag,
            "options": self.options
        }

    @classmethod
    def from_dict(cls, d):
        obj = cls()
        obj.name = d["name"]
        obj.abbr = d["abbr"]
        obj.type = UExpressionType(d["type"])
        obj.minValue = d["min"]
        obj.maxValue = d["max"]
        obj.defaultValue = d["default_value"]
        obj.isFlags = d.get("is_flags", False)
        obj.flag = d.get("flag", "")
        obj.options = d.get("options", None)
        return obj

class UExpression:
    descriptor:UExpressionDescriptor
    _value:float = 0
    index: Optional[int] = None
    abbr:str
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if(descriptor==null):
            self._value = value
        else:
            self._value = max(min(value, descriptor.maxValue), descriptor.minValue)

    def __init__(
            self, 
            descriptor:Optional[UExpressionDescriptor] = None, 
            abbr:str = "",
        ):
        if(descriptor is None):
            self.abbr = abbr
            return
        self.descriptor = descriptor
        self.abbr = descriptor.abbr