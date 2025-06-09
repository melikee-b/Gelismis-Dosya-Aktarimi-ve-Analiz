import socket
import time

HOST = '127.0.0.1'  # Sunucu IP'si
PORT = 5001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print("[+] Sunucuya bağlanıldı.")

    # RTT testini 10 kez yapalım
    for i in range(10):
        msg = b"ping"
        start = time.time()
        client_socket.sendall(msg)
        data = client_socket.recv(1024)
        end = time.time()

        rtt = (end - start) * 1000  # RTT’yi milisaniye cinsinden al
        print(f"Ping {i+1}: RTT = {rtt:.3f} ms")
