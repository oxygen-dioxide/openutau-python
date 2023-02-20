#reference: https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/Ustx/UNote.cs
import enum
from typing import List, Type

class PitchPointShape(enum.Enum):
    io = "io"
    l = "1"
    i = "i"
    o = "o"

class PitchPoint:
    X:float = 0.0
    Y:float = 0.0
    Shape:PitchPointShape  = PitchPointShape.io

    def __init__(self, x:float, y:float, shape:PitchPointShape):
        self.X = x
        self.Y = y
        self.Shape = shape

    def __lt__(self, other:Type["PitchPoint"]) -> bool:
        return self.X < other.X
    
    def __gt__(self, other:Type["PitchPoint"]) -> bool:
        return self.X > other.X

    def to_dict(self):
        return {
            "x": self.X,
            "y": self.Y,
            "shape": self.Shape.value
        }
    
    @classmethod
    def from_dict(cls, d:dict):
        return cls(d["x"], d["y"], PitchPointShape(d["shape"]))

class UPitch:
    data:List[PitchPoint] = []
    snapFirst:bool = True

    def AddPoint(self, p:PitchPoint):
        self.data.append(p)
        self.data.sort()
    
    def RemovePoint(self, p:PitchPoint):
        self.data.remove(p)
    
    def to_sict(self):
        return {
            "snapFirst": self.snapFirst,
            "data": [p.to_dict() for p in self.data]
        }
    
    @classmethod
    def from_dict(cls, d:dict):
        pitch = cls()
        pitch.snapFirst = d["snap_first"]
        pitch.data = [PitchPoint.from_dict(p) for p in d["data"]]
        return pitch

class UVibrato:
    # Vibrato percentage of note length.
    _length:float = 0.0
    # Period in milliseconds.
    _period:float = 0.0
    # Depth in cents (1 semitone = 100 cents).
    _depth:float = 0.0
    # Fade-in percentage of vibrato length.
    _fadein:float = 0.0
    # Fade-out percentage of vibrato length.
    _fadeout:float = 0.0
    # Shift percentage of period length.
    _shift:float = 0.0
    _drift:float = 0.0

    @property
    def length(self) -> float:
        return self._length
    
    @length.setter
    def length(self, value:float):
        self._length = max(0.0, min(100.0, value))

    @property
    def period(self) -> float:
        return self._period
    
    @period.setter
    def period(self, value:float):
        self._period = max(5.0, min(500.0, value))

    @property
    def depth(self) -> float:
        return self._depth
    
    @depth.setter
    def depth(self, value:float):
        self._depth = max(5.0, min(200.0, value))
    
    @property
    def fadein(self) -> float:
        return self._fadein
    
    @fadein.setter
    def fadein(self, value:float):
        self._fadein = max(0.0, min(100.0, value))
        self._fadeout = min(self._fadeout, 100.0 - self._fadein)
    
    @property
    def fadeout(self) -> float:
        return self._fadeout
    
    @fadeout.setter
    def fadeout(self, value:float):
        self._fadeout = max(0.0, min(100.0, value))
        self._fadein = min(self._fadein, 100.0 - self._fadeout)

    @property
    def shift(self) -> float:
        return self._shift
    
    @shift.setter
    def shift(self, value:float):
        self._shift = max(0.0, min(100.0, value))

    @property
    def drift(self) -> float:
        return self._drift
    
    @drift.setter
    def drift(self, value:float):
        self._drift = max(-100.0, min(100.0, value))\
    
    def NormalizedStart(self) -> float:
        return (1-length)/100.0
    
    #TODO

    @classmethod
    def from_dict(cls, d:dict):
        vibrato = cls()
        vibrato.length = d["length"]
        vibrato.period = d["period"]
        vibrato.depth = d["depth"]
        vibrato.fadein = d["in"]
        vibrato.fadeout = d["out"]
        vibrato.shift = d["shift"]
        vibrato.drift = d["drift"]

    def to_dict(self):
        return {
            "length": self.length,
            "period": self.period,
            "depth": self.depth,
            "in": self.fadein,
            "out": self.fadeout,
            "shift": self.shift,
            "drift": self.drift
        }

class UNote:
    position:int = 0
    duration:int = 0
    tone:int = 60
    lyric:str = "a"
    pitch:UPitch = UPitch()
    vibrato:UVibrato = UVibrato()

    def __str__(self):
        return f"\"{lyric}\" Pos:{position} Dur:{duration} Tone:{tone}{(string.Empty)}{(string.Empty)}"
    
    def __repr__(self):
        return self.__str__()

    def __gt__(self, other:Type["UNote"]) -> bool:
        if(self.position == other.position):
            return hash(self) > hash(other)
        else:
            return self.position > other.position
    
    def __lt__(self, other:Type["UNote"]) -> bool:
        if(self.position == other.position):
            return hash(self) < hash(other)
        else:
            return self.position < other.position

    @classmethod
    def from_dict(cls, d:dict):
        note = cls()
        note.position = d["position"]
        note.duration = d["duration"]
        note.tone = d["tone"]
        note.lyric = d["lyric"]
        note.pitch = UPitch.from_dict(d["pitch"])
        note.vibrato = UVibrato.from_dict(d["vibrato"])
        return note
    
    def to_dict(self):
        return {
            "position": self.position,
            "duration": self.duration,
            "tone": self.tone,
            "lyric": self.lyric,
            "pitch": self.pitch.to_dict(),
            "vibrato": self.vibrato.to_dict()
        }
