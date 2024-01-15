import os
import torch
import torchaudio
import soundfile as sf
from IPython.display import Audio

import torchaudio.functional as F

print(torch.__version__)
print(torchaudio.__version__)

import matplotlib.pyplot as plt

def apply_codec(waveform, sample_rate, format, encoder=None):
    encoder = torchaudio.io.AudioEffector(format=format, encoder=encoder)
    return encoder.apply(waveform, sample_rate)

def saveAudio(audio, waveform, codec):
  if codec == "mulaw":
    dir = "/hkfs/home/haicore/hgf_cispa/hgf_yie2732/BaselineDatasets/LA/ASVspoof2019_LA_eval/mu-law/" + str(audio)
  elif codec == "g772":
    dir = "/hkfs/home/haicore/hgf_cispa/hgf_yie2732/BaselineDatasets/LA/ASVspoof2019_LA_eval/g772/" + str(audio)
  else:
    dir = "/hkfs/home/haicore/hgf_cispa/hgf_yie2732/BaselineDatasets/LA/ASVspoof2019_LA_eval/vorbis/" + str(audio)

  sf.write(dir, waveform, 16000)

dir_list = os.listdir('/hkfs/home/haicore/hgf_cispa/hgf_yie2732/BaselineDatasets/LA/ASVspoof2019_LA_eval/wav/')
dir_list = sorted(dir_list)
ctr = 0
print(dir_list)

for audio in dir_list:
  ctr += 1
  print(ctr, audio)
  try:
    waveform, sample_rate = torchaudio.load('/hkfs/home/haicore/hgf_cispa/hgf_yie2732/BaselineDatasets/LA/ASVspoof2019_LA_eval/wav/' + str(audio), channels_first=False)
    mulaw = apply_codec(waveform, sample_rate, "wav", encoder="pcm_mulaw")
    #g772 = apply_codec(waveform, sample_rate, "wav", encoder="g722")
    #vorbis = apply_codec(waveform, sample_rate, "wav", encoder="vorbis")
    saveAudio(audio, mulaw, "mulaw")
    #saveAudio(audio, g772, "g772")
    #saveAudio(audio, vorbis, "vorbis")
  except:
    print("Failed Conversion:", audio)
