import matplotlib.pyplot as plt

# Örnek RTT değerleri (milisaniye cinsinden)
rtt_values = [0.87, 0.75, 0.65, 0.9, 0.8, 0.78, 0.85, 0.82, 0.8, 0.9]

# X ekseni (ping numarası)
ping_numbers = [i+1 for i in range(len(rtt_values))]

# Grafik çizimi
plt.plot(ping_numbers, rtt_values, marker='o', linestyle='-', color='b', label='RTT (ms)')

# Başlık ve eksen isimleri
plt.title("RTT (Round Trip Time) Değerleri")
plt.xlabel("Ping Denemesi")
plt.ylabel("RTT (ms)")

# Efsane ve grid
plt.legend()
plt.grid(True)

# Grafiği göster
plt.show()
