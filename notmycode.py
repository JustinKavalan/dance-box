import numpy as np
import matplotlib.pyplot as plt
import sounddevice
from scipy.io import wavfile as wav

fs, wave = wav.read('piano1.wav')

#fs is sampling frequency
# fs = 20000
length = wave.shape[0] / fs
time = np.linspace(0,length,int(length*fs),endpoint=False)
# freq_signal = 1000

#wave is the sum of sine wave(1Hz) and cosine wave(10 Hz)
# wave = np.sin(np.pi*time)+ np.cos(np.pi*time)
# wave = [np.sin(2 * np.pi * freq_signal * x1) for x1 in time]
wave = np.array(wave)
wave = wave[:,1]
print(wave.shape)
# sounddevice.play(wave, fs)
#wave = np.exp(2j * np.pi * time )

plt.plot(time, wave)
plt.xlim(0, length)
plt.xlabel("time (second)")
plt.title('Original Signal in Time Domain')

plt.show()

# Compute the one-dimensional discrete Fourier Transform.

fft_wave = np.fft.fft(wave)
cur_max = (np.maximum(fft_wave.max(), np.abs(fft_wave.min())))
# print(np.int(cur_max))
fft_wave = fft_wave / cur_max.real
# Compute the Discrete Fourier Transform sample frequencies.

fft_fre = np.fft.fftfreq(n=wave.shape[0], d=1/fs)

plt.subplot(211)
plt.plot(fft_fre, fft_wave.real, label="Real part")
plt.xlim(-20000,20000)
plt.ylim(-1,1)
plt.legend(loc=1)
plt.title("FFT in Frequency Domain")

plt.subplot(212)
plt.plot(fft_fre, fft_wave.imag,label="Imaginary part")
plt.xlim(-20000,20000)
plt.ylim(-600,600)
plt.legend(loc=1)
plt.xlabel("frequency (Hz)")

plt.show()