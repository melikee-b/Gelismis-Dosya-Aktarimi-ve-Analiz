import socket

# Bağlantı ayarları
HOST = '192.168.56.1' 
PORT = 5001

# Gönderilecek büyük dosya
FILENAME = 'large_test_file.txt'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print("[+] Sunucuya bağlanıldı. Dosya gönderiliyor...")

    with open(FILENAME, 'rb') as f:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            client_socket.sendall(chunk)
            print("[>] Parça gönderildi...")

print("[+] Dosya gönderimi tamamlandı.")
