import essentia.standard as es
import os 
import numpy as np

def get_audio_info(audio_path : str) -> list:
  audio = es.MonoLoader(filename=audio_path)()
  bpm,beats,beats_confidence,_,beats_intervals = rhythm_extractor = es.RhythmExtractor2013(method="multifeature")(audio)
  return [bpm, beats, beats_intervals]

def read_files(folder_path : str) -> str:
  files = os.listdir(folder_path)
  return files

def get_beat(audio_path : str) -> str:
  bpm, beats, beat_intervals = get_audio_info(audio_path)
  beat_intervals = np.diff(beats)
  mean_interval = np.mean(beat_intervals)
  std_interval = np.std(beat_intervals)
  
  # 박자 판단 기준
  """
  강세의 개수로 따지는 박자임. 
  강세가 4개단위로 나타난다면 4/4
  강세가 3개단위로 나타난다면 3/4
  만약 강세가 알 수 없게 나오면 4/4로 따지려고 함. (가장 보편적임.) 
  """
  if len(beat_intervals) % 3 == 0:
    time_signature = "3/4"
  else:
    time_signature = "4/4"
  
  return time_signature