#!/usr/bin/env python3

from scipy.fft import fft
from scipy.io import wavfile as wav
from scipy import signal
import matplotlib.pyplot as plt
import os
import numpy as np

sampling_rate=44100
freq_signal=10000
num_samples=3000000
# num_samples=10000
fs = 10e3

# fs, audio = wav.read('piano2.wav')
# print(fs)
# audio = np.average(audio, axis=1)
# audio = audioSource.readframes(audioSource.getnframes())
audio = [np.sin(2 * np.pi * freq_signal * x1/sampling_rate) for x1 in range(num_samples)]
audio = np.array(audio)
res = np.fft.fft(audio)
print(res)
print(res.shape)
print(res.argmax() / sampling_rate)

fre = np.fft.fftfreq(num_samples, 1/sampling_rate)

# f, t, Sxx = signal.spectrogram(audio, fs)
time = np.linspace(0, num_samples/sampling_rate, num_samples)
plt.plot(time, audio, label="Real")
plt.xlim(-50,50)
plt.ylim(-20000,20000)
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
plt.show()
