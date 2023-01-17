from .builder import FEATURE_EXTRACTORS
from .chinese_hubert import ChineseHubert
from .hubert_soft import HubertSoft
from .wav2vec2_xlsr import Wav2Vec2XLSR

__all__ = ["ChineseHubert", "Wav2Vec2XLSR", "FEATURE_EXTRACTORS", "HubertSoft"]
