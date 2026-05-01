import numpy as np
import matplotlib.pyplot as plt

# Time axis
t = np.linspace(0, 1, 1000)

# Original signal (sine wave)
signal = np.sin(2 * np.pi * 5 * t)

# -----------------------------
# 1. AWGN (Additive White Gaussian Noise)
# -----------------------------
mean = 0
variance = 0.1
awgn = np.random.normal(mean, np.sqrt(variance), len(t))
signal_awgn = signal + awgn

# -----------------------------
# 2. Thermal Noise (similar to AWGN but lower variance)
# -----------------------------
thermal_noise = np.random.normal(0, 0.05, len(t))
signal_thermal = signal + thermal_noise

# -----------------------------
# 3. Impulse Noise (sudden spikes)
# -----------------------------
impulse_noise = np.zeros(len(t))
num_spikes = 20
indices = np.random.randint(0, len(t), num_spikes)
impulse_noise[indices] = np.random.choice([2, -2], num_spikes)
signal_impulse = signal + impulse_noise

# -----------------------------
# 4. Random Noise (general random variation)
# -----------------------------
random_noise = np.random.uniform(-0.5, 0.5, len(t))
signal_random = signal + random_noise

# -----------------------------
# Plotting
# -----------------------------
plt.figure(figsize=(12, 10))

plt.subplot(5,1,1)
plt.plot(t, signal)
plt.title("Original Signal")

plt.subplot(5,1,2)
plt.plot(t, signal_awgn)
plt.title("Signal with AWGN")

plt.subplot(5,1,3)
plt.plot(t, signal_thermal)
plt.title("Signal with Thermal Noise")

plt.subplot(5,1,4)
plt.plot(t, signal_impulse)
plt.title("Signal with Impulse Noise")

plt.subplot(5,1,5)
plt.plot(t, signal_random)
plt.title("Signal with Random Noise")

plt.tight_layout()
plt.show()