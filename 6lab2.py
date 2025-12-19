import numpy as np
import matplotlib.pyplot as plt

betamin = 15

Rz = 6371218  # Радиус Земли в метрах
h = np.linspace(200000, 30000000, 100)  # Высота в метрах
b = betamin * (np.pi / 180)  # Угол места в радианах (15 градусов)

# Расчет угла тета
teta = np.arccos((Rz * np.cos(b)) / (Rz + h)) - b

plt.figure(figsize=(10, 6))
plt.plot(h / 1000, np.degrees(teta))
plt.xlabel("h, км")
plt.ylabel("θ, °", rotation=0, labelpad=15)
plt.title("Зависимость θ от высоты h")
plt.grid(True)
plt.tight_layout()
plt.show()