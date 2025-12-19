import numpy as np
import matplotlib.pyplot as plt

ampl_1 = 6
ampl_2 = 9
ampl_3 = 12
ampl_4 = 15
ampl_5 = 18

f1 = 1
f2 = 5
f3 = 10
f4 = 15
f5 = 20

min_limit_x = 0
max_limit_x = 1
N = 1024

mean = 9
sigma = 11

massive_normal = np.random.normal(mean, sigma, N)

fd = N/max_limit_x
x = np.linspace(min_limit_x, max_limit_x, N)
massive_sin1 = ampl_1 * np.sin(2*np.pi*f1*x)
massive_sin2 = ampl_2 * np.sin(2*np.pi*(f2)*x)
massive_sin3 = ampl_3 * np.sin(2*np.pi*(f3)*x)
massive_sin4 = ampl_4 * np.sin(2*np.pi*(f4)*x)
massive_sin5 = ampl_5 * np.sin(2*np.pi*(f5)*x)

add_sig = massive_sin1  + massive_sin2 + massive_sin3 + massive_sin4 + massive_sin5
Q = add_sig + massive_normal

plt.figure(1)
plt.title("1 синусоида")
plt.plot(x, massive_sin1)
plt.grid("on")

plt.figure(2)
plt.title("2 синусоида")
plt.plot(x, massive_sin2)
plt.grid("on")

plt.figure(3)
plt.title("3 синусоида")
plt.plot(x, massive_sin3)
plt.grid("on")

plt.figure(4)
plt.title("4 синусоида")
plt.plot(x, massive_sin4)
plt.grid("on")

plt.figure(5)
plt.title("5 синусоида")
plt.plot(x, massive_sin5)
plt.grid("on")

plt.figure(6)
plt.title("Сумма синусоид без шума")
plt.plot(x, add_sig)
plt.grid("on")

plt.figure(7)
plt.title("Сумма синусоид c аддитивным шумом")
plt.plot(x, Q)
plt.grid("on")

M = 4*N
f_range = np.zeros(M)
for smp_ref in range(-int(M/2), int(M/2)):
    f_range[smp_ref] = (smp_ref / M)* fd

fft_result = np.fft.fft(Q, M)/N
mod_fftshift_result = abs(fft_result)

plt.figure(8)
plt.title("Спектр сигнала с АЧХ фильтра для наглядности")
plt.plot(f_range, mod_fftshift_result)
plt.grid("on")

a4h = np.zeros(M)
freq_rez = 12
polosa = 20

min_a4h_freq = freq_rez - (polosa/2)
max_a4h_freq = freq_rez + (polosa/2)

for smp_ref in range(-int(M/2), int(M/2)):
    if (f_range[smp_ref] > min_a4h_freq):
        if (f_range[smp_ref] < max_a4h_freq):
            a4h[smp_ref] = 1
    if (f_range[smp_ref] < -min_a4h_freq):
        if (f_range[smp_ref] > -max_a4h_freq):
            a4h[smp_ref] = 1
            
plt.figure(8)
plt.plot(f_range, a4h)
plt.grid("on")

filtered_add_smes_spektr = a4h*fft_result
filtered_add_smes = N*np.fft.ifft(filtered_add_smes_spektr)

plt.figure(9)
plt.plot(f_range, abs(filtered_add_smes_spektr))
plt.grid("on")

invert_fft_mas_len = int(len(filtered_add_smes)*N/M)

plt.figure(10)
plt.title("Сигнал после ОПФ")
plt.plot(x, filtered_add_smes[0:invert_fft_mas_len])
plt.grid("on")

resultT = add_sig - filtered_add_smes[0:invert_fft_mas_len]

plt.figure(11)
plt.title("Итоговый график")
plt.plot(x, resultT)
plt.grid("on")


