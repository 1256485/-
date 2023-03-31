# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 23:17:34 2023

@author: ljhdy
"""

# Importing the necessary library
import numpy as np
import matplotlib.pyplot as plt

# Defining the signal
t = np.linspace(0, 1, 500)
f = 5  # Frequency in Hz
signal = np.sin(2 * np.pi * f * t)

# Performing Fourier transform
fourier_transform = np.fft.fft(signal)

# Plotting the signal and its Fourier transform
fig, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].plot(t, signal)
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Amplitude')
axs[0].set_title('Signal')
axs[1].plot(np.abs(fourier_transform))
axs[1].set_xlabel('Frequency (Hz)')
axs[1].set_ylabel('Amplitude')
axs[1].set_title('Fourier Transform')
plt.tight_layout()
plt.show()
