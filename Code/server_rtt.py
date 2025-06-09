import socket

HOST = '0.0.0.0'
PORT = 5001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print("[+] RTT Sunucusu dinleniyor...")

    conn, addr = server_socket.accept()
    with conn:
        print("[+] Bağlantı sağlandı:", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)  # Gelen veriyi aynen geri gönder

