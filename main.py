# Audio Attempt
from pydub import AudioSegment
import numpy as np

# Set the desired frequency (400Hz in this case)
frequency = 400  # in Hertz

# Set the duration of the audio segment (e.g., 5 seconds)
duration_seconds = 5
duration_milliseconds = int(duration_seconds * 1000)  # convert to milliseconds

# Generate a sine wave signal
t = np.linspace(0, duration_seconds, int(duration_seconds * 44100), endpoint=False)
signal = 0.5 * np.sin(2 * np.pi * frequency * t)

# Convert the numpy array to Pydub's AudioSegment
audio_segment = AudioSegment(signal.tobytes(), frame_rate=44100, sample_width=signal.dtype.itemsize, channels=1)

# Play the audio segment
audio_segment.play()