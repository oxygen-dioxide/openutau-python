#reference: https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/Ustx/UPart.cs
from sortedcontainers import SortedSet
from typing import List

from .unote import UNote
from .ucurve import UCurve

class UPart:
    name:str = "New Part"
    comment:str = ""
    trackNo:int = 0
    position:int = 0

class UVoicePart(UPart):
    notes:SortedSet[UNote] = SortedSet()
    curves:List[UCurve] = []

    def to_dict(self):
        return {
            "name": self.name,
            "comment": self.comment,
            "track_no": self.trackNo,
            "position": self.position,
            "notes": [note.to_dict() for note in self.notes],
            "curves": [curve.to_dict() for curve in self.curves],
        }
    
    @classmethod
    def from_dict(cls, d):
        obj = cls()
        obj.name = d["name"]
        obj.comment = d["comment"]
        obj.trackNo = d["track_no"]
        obj.position = d["position"]
        obj.notes = SortedSet([UNote.from_dict(note) for note in d["notes"]])
        obj.curves = [UCurve.from_dict(curve) for curve in d["curves"]]
        return obj
    
class UWavePart(UPart):
    _filePath:str = ""
    relativePath:str = ""
    fileDurationMs:float = 0.0
    skipMs:float = 0.0
    trimMs:float = 0.0

    def to_dict(self):
        return {
            "name": self.name,
            "comment": self.comment,
            "track_no": self.trackNo,
            "position": self.position,
            "relative_path": self.relativePath,
            "file_duration_ms": self.fileDurationMs,
            "skip_ms": self.skipMs,
            "trim_ms": self.trimMs,
        }
    
    @classmethod
    def from_dict(cls, d):
        obj = cls()
        obj.name = d["name"]
        obj.comment = d["comment"]
        obj.trackNo = d["track_no"]
        obj.position = d["position"]
        obj.relativePath = d["relative_path"]
        obj.fileDurationMs = d["file_duration_ms"]
        obj.skipMs = d["skip_ms"]
        obj.trimMs = d["trim_ms"]
        return obj
    

    