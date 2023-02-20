#reference: https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/Ustx/UTrack.cs

from typing import List,Dict,Optional

class URenderSettings:
    renderer:Optional[str] = None
    resampler:Optional[str] = None
    wavtool:Optional[str] = None

    def to_dict(self):
        return {
            "renderer": self.renderer,
            "resampler": self.resampler,
            "wavtool": self.wavtool,
        }
    
    @classmethod
    def from_dict(cls, d):
        obj = cls()
        obj.renderer = d.get("renderer", None)
        obj.resampler = d.get("resampler", None)
        obj.wavtool = d.get("wavtool", None)
        return obj

class UTrack:
    singer:Optional[str] = None
    phonemizer:str
    renderSettings:URenderSettings
    mute:bool = False
    solo:bool = False
    volume:float = 0.0

    def to_dict(self):
        return {
            "singer": self.singer,
            "phonemizer": self.phonemizer,
            "render_settings": self.renderSettings.to_dict(),
            "mute": self.mute,
            "solo": self.solo,
            "volume": self.volume,
        }
    @classmethod
    def from_dict(cls, d):
        obj = cls()
        obj.singer = d.get("singer", None)
        obj.phonemizer = d["phonemizer"]
        if(d.get("render_settings", None) is None):
            obj.renderSettings = URenderSettings()
        else:
            obj.renderSettings = URenderSettings.from_dict(d["render_settings"])
        obj.mute = d["mute"]
        obj.solo = d["solo"]
        obj.volume = d["volume"]
        return obj