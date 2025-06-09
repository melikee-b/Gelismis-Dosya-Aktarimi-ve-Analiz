import socket
from aes_utils import decrypt_data

# Ayarlar
HOST = '0.0.0.0'

PORT = 5001
KEY = b'ThisIsA16ByteKey'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print("[+] Sunucu dinleniyor...")

    conn, addr = server_socket.accept()
    with conn:
        print("[+] Bağlantı sağlandı:", addr)
        encrypted_data = b''

        while True:
            data = conn.recv(1024)
            if not data:
                break
            encrypted_data += data

        # AES ile çöz
        decrypted_data = decrypt_data(encrypted_data, KEY)

        # Çözülen veriyi dosyaya kaydet
        with open('received_decrypted_file.txt', 'wb') as f:
            f.write(decrypted_data)

print("[+] Şifreli dosya başarıyla alındı ve çözüldü.")
