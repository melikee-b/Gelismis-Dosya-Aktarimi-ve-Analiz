import socket

# Sunucu ayarları
HOST = '0.0.0.0'  # Tüm arayüzlerden bağlantı kabul et
PORT = 5001       # Kullanılacak port

# Dosya oluşturma
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print("[+] Sunucu dinleniyor...")

    conn, addr = server_socket.accept()
    with conn:
        print("[+] Bağlantı sağlandı:", addr)
        
        # Gelen parçaları kaydetmek için boş dosya oluştur
        with open('received_large_file.txt', 'wb') as f:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)
                print("[>] Parça alındı ve eklendi...")

print("[+] Dosya alma tamamlandı. Dosya: received_large_file.txt")
