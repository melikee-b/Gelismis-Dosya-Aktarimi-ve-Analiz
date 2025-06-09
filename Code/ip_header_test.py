from scapy.all import IP, ICMP, send

# IP başlığı ve ICMP oluştur
ip_pkt = IP(dst="8.8.8.8")  # Örneğin Google DNS'e gönderiyoruz
ip_pkt.ttl = 64             # Time to Live değerini 64 olarak ayarla
ip_pkt.flags = "DF"         # Don't Fragment flag'i ayarla
ip_pkt.id = 12345           # ID alanını ayarla

# Checksum'ı elle hesaplatmak için (Scapy otomatik hesaplıyor aslında)
ip_pkt.chksum = None  # None verirsen Scapy otomatik hesaplayacak

icmp_pkt = ICMP()

# Paketi oluştur ve gönder
pkt = ip_pkt / icmp_pkt
send(pkt)

print("Paket gönderildi!")
