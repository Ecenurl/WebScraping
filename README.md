# WebScraping
Bu proje, bir e-ticaret sitesinden (http://books.toscrape.com/) kitap verilerini çekerek başlık ve fiyat bilgilerini toplamayı, bu verileri analiz etmeyi ve CSV dosyasına kaydetmeyi amaçlamaktadır.

🛠 Kullanılan Teknolojiler
Python

Requests

BeautifulSoup

Pandas

📋 Proje Adımları
Web sitesinden HTML verisi çekildi (requests modülü ile).

HTML içeriği parse edildi (BeautifulSoup ile).

Kitap başlıkları ve fiyatlar sayfadan ayrıştırıldı.

Veriler liste yapısında saklandı.

Pandas ile tablo (DataFrame) oluşturuldu.

Sonuçlar bir .csv dosyasına kaydedildi.

📦 Kurulum
Projeyi çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekiyor:

bash
Kopyala
Düzenle
pip install requests beautifulsoup4 pandas
🚀 Kullanım
Projeyi çalıştırmak için:

bash
Kopyala
Düzenle
python main.py
Çalıştıktan sonra books_data.csv adında bir dosya oluşacak ve tüm kitap isimleri ile fiyatları burada saklanacak.

📊 Örnek Çıktı

Title	Price
A Light in the Attic	51.77
Tipping the Velvet	53.74
Soumission	50.10
...	...
🎯 Amaç
Web scraping pratiği kazanmak

Veri temizleme ve analiz becerilerini geliştirmek

Verileri CSV formatına kaydetmeyi öğrenmek

📌 Not: Proje eğitim amaçlı hazırlanmıştır. Gerçek sitelerde scraping yaparken sitenin kullanım şartlarına dikkat edilmelidir.

📬 İletişim
Ecenur Yılmaz
GitHub Profilim

