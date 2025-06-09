import socket

# Sunucu ayarları
server_ip = "127.0.0.1"
server_port = 5005
buffer_size = 1024

# Soket oluştur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))
print("[+] UDP sunucu dinleniyor:", (server_ip, server_port))

while True:
    # Veri al
    data, client_addr = server_socket.recvfrom(buffer_size)
    print(f"[+] Paket alındı: {data.decode()}")

    # ACK gönder
    ack_message = "ACK".encode()
    server_socket.sendto(ack_message, client_addr)
    print(f"[+] ACK gönderildi -> {client_addr}")
