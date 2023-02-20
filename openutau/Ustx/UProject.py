#reference: https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/Ustx/UProject.cs

from typing import List,Dict

from .uexpression import UExpressionDescriptor
from .utrack import UTrack
from .upart import UVoicePart, UWavePart

class UTempo:
    position:int
    bpm:float
    def __init__(self, position:int, bpm:float):
        self.position = position
        self.bpm = bpm
    
    def __str__(self):
        return f"{self.bpm}@{self.position}"
    
    def to_dict(self):
        return {
            "position": self.position,
            "bpm": self.bpm,
        }
    
    @classmethod
    def from_dict(cls, d):
        obj = cls(d["position"], d["bpm"])
        return obj

#UTimeSignature isn't currently supported in openutau-python
#Defaults to 4/4
#Until OpenUtau fix bug with time signature in classic wavtools

class UProject:
    name:str
    comment:str = ""
    outputDir:str = "Vocal"
    cacheDir:str = "UCache"

    bpm:float = 120.0
    expressions:Dict[str, UExpressionDescriptor] = {}
    tempos:List[UTempo] = []
    tracks:List[UTrack] = []
    voiceParts:List[UVoicePart] = []
    waveParts:List[UWavePart] = []

    def __init__(self):
        self.tempos = [UTempo(0,120)]
    
    def to_dict(self):
        return {
            "name": self.name,
            "comment": self.comment,
            "output_dir": self.outputDir,
            "cache_dir": self.cacheDir,
            "bpm": self.bpm,
            "expressions": {abbr:desc.to_dict() for abbr,desc in self.expressions.items()},
            "tempos": [tempo.to_dict() for tempo in self.tempos],
            "tracks": [track.to_dict() for track in self.tracks],
            "voice_parts": [part.to_dict() for part in self.voiceParts],
            "wave_parts": [part.to_dict() for part in self.waveParts],
        }
    
    @classmethod
    def from_dict(cls, d):
        obj = cls()
        obj.name = d["name"]
        obj.comment = d["comment"]
        obj.outputDir = d["output_dir"]
        obj.cacheDir = d["cache_dir"]
        obj.bpm = d["bpm"]
        obj.expressions = {abbr:UExpressionDescriptor.from_dict(desc) for abbr,desc in d["expressions"].items()}
        obj.tempos = [UTempo.from_dict(tempo) for tempo in d["tempos"]]
        obj.tracks = [UTrack.from_dict(track) for track in d["tracks"]]
        obj.voiceParts = [UVoicePart.from_dict(part) for part in d["voice_parts"]]
        obj.waveParts = [UWavePart.from_dict(part) for part in d["wave_parts"]]
        return obj
    
