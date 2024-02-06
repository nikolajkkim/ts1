import audioop
import wave
import numpy as np

# set the desired frequency 
frequency = 400  # in Hertz

duration_seconds = 5
sample_rate = 44100
num_frames = int(duration_seconds * sample_rate)

# generate a sine wave signal
t = np.linspace(0, duration_seconds, num_frames, endpoint=False)
signal = 0.5 * np.sin(2 * np.pi * frequency * t)

# scale the signal to fit in the range of a 16-bit PCM (pulse code modulation) audio file
# the term "16-bit" refers to the number of bits used to represent the amplitude of each sample in the audio signal
scaled_signal = np.int16(signal * 32767)

# save the signal to a WAV file
output_path = 'output_audio.wav'
with wave.open(output_path, 'w') as wav_file:
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(scaled_signal.tobytes())

# play the audio using the 'afplay' command on macOS or 'start' on Windows
import subprocess
subprocess.run(['afplay', output_path]) 
# subprocess.run(['start', 'output_audio.wav'], shell=True)  # For Windows... jake



