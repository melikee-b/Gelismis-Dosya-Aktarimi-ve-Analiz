import socket
from aes_utils import encrypt_data

# Ayarlar
HOST = '127.0.0.1'
  # Sunucu IP'si
PORT = 5001
KEY = b'ThisIsA16ByteKey'  # 16 byte (128 bit) AES key

# Gönderilecek dosya
FILENAME = 'large_test_file.txt'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print("[+] Sunucuya bağlanıldı. Şifreli dosya gönderiliyor...")

    with open(FILENAME, 'rb') as f:
        file_data = f.read()

    # AES ile şifrele
    encrypted_data = encrypt_data(file_data, KEY)
    client_socket.sendall(encrypted_data)

print("[+] Şifreli dosya gönderimi tamamlandı.")
