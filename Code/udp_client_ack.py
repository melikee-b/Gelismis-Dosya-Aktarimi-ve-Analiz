import socket
import time

# İstemci ayarları
server_ip = "127.0.0.1"
server_port = 5005
buffer_size = 1024
timeout_sec = 1.0  # ACK bekleme süresi

# Soket oluştur
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(timeout_sec)

# Gönderilecek paketler
packets = [f"Packet {i+1}" for i in range(10)]

for packet in packets:
    while True:
        try:
            # Paketi gönder
            client_socket.sendto(packet.encode(), (server_ip, server_port))
            print(f"[>] Paket gönderildi: {packet}")

            # ACK bekle
            ack_data, _ = client_socket.recvfrom(buffer_size)
            if ack_data.decode() == "ACK":
                print("[<] ACK alındı!")
                break  # ACK alındı, sonraki pakete geç
        except socket.timeout:
            print("[!] ACK alınamadı, tekrar gönderiliyor...")
            time.sleep(0.5)  # Küçük bir bekleme

print("[+] Tüm paketler başarıyla gönderildi.")
client_socket.close()

