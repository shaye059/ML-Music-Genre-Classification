import librosa
import matplotlib as plt
import librosa.display

file_path = '/Users/nicolaspare/GitRepo/ML-Music-Classifier/main/resources/genres/hiphop/hiphop.00000.wav'
x , sr = librosa.load(file_path)

plt.figure(figsize=(20, 6))
librosa.display.waveplot(x, sr=sr)
