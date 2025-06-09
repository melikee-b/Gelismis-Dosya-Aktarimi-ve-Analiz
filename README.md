# Gelişmiş Dosya Transfer Sistemi: Şifreleme, Düşük Seviyeli IP İşleme ve Ağ Performans Analizi

Bu proje, Python socket programlama kullanarak **güvenli ve hızlı dosya aktarımı** sağlayan gelişmiş bir istemci-sunucu sistemidir. Dosya transferinin yanı sıra **AES şifreleme**, **SHA256 bütünlük kontrolü**, **düşük seviyeli IP başlık manipülasyonu** ve **ağ performans analizi** gibi önemli konuları da kapsar.

---

## 🚀 Özellikler

✅ **Büyük Dosya Transferi**  
- Dosya, 1024 baytlık parçalara bölünerek transfer edilir.  
- Sunucu, parçaları eksiksiz şekilde alıp birleştirir.

✅ **AES Şifreleme & SHA256 Doğrulama**  
- AES şifreleme ile verinin gizliliği sağlanır.  
- SHA256 hash kontrolü ile veri bütünlüğü doğrulanır.

✅ **Düşük Seviyeli IP İşleme**  
- IP başlığında TTL, checksum gibi alanlar manipüle edilir.  
- Wireshark kullanılarak veri akışı analiz edilir.

✅ **UDP ACK/NACK Hata Yönetimi**  
- UDP ile gönderilen verilerin güvenilir şekilde aktarımı için ACK/NACK sistemi.

✅ **Ağ Performans Testleri**  
- RTT ölçümü (Round Trip Time).  
- iPerf3 ile loopback ve WiFi üzerinden bant genişliği testi.  
- Matplotlib ile RTT ve bant genişliği grafik analizi.

---

## ⚙️ Kullanılan Teknolojiler

- **Python 3**
- **cryptography** kütüphanesi (AES şifreleme)  
- **hashlib** (SHA256 hash)  
- **socket** (TCP & UDP)  
- **Scapy** (IP header manipülasyonu)  
- **Wireshark** (Ağ trafiği analizi)  
- **iPerf3** (Bant genişliği testi)  
- **Matplotlib** (Grafik çizimleri)

---

## 📂 Proje Dosyaları

- `client_chunked.py` & `server_chunked.py`: Dosya transferi.  
- `sha256_checker.py`: Dosya bütünlüğü doğrulama.  
- `server_rtt.py` & `client_rtt.py`: RTT ölçümü.  
- `udp_server_ack.py` & `udp_client_ack.py`: UDP hata yönetimi.  
- `iperf3_testler/`: iPerf3 test çıktıları.  
- `rtt_plot.py`: RTT grafik analizi.  
- `bandwidth_plot.py`: Bant genişliği grafik analizi.

---

## 🎯 Sonuç ve Katkı

Bu proje, güvenilir ve hızlı dosya aktarımı yaparken aynı zamanda ağ performansını analiz etmeyi ve veri bütünlüğünü sağlamayı amaçlamaktadır.🚀✨

---

📹 **Proje Açıklama Videosu:**  
👉 [YouTube Linki](https://youtu.be/pJFZ6lGiv5M)

