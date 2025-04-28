import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)

# Sayfa başarıyla yüklendi mi kontrol edelim
if response.status_code == 200:
    print("Sayfa başarıyla yüklendi!")
else:
    print(f"Sayfa yüklenemedi! Hata kodu: {response.status_code}")
    exit()

# Sayfa içeriğini parse et
soup = BeautifulSoup(response.text, "html.parser")

# Kitap başlıklarını çekelim
books = soup.find_all('h3')

book_titles = []
book_prices = []

for book in books:
    # Kitap başlığını alalım
    title = book.find('a')['title']
    book_titles.append(title)
    
    # Fiyatı alalım
    price_tag = book.find_next('p', class_='price_color')
    if price_tag:
        price = price_tag.text
        print(f"Orijinal Fiyat: {price}")
        
        # Garip karakterleri temizleyelim ve sayıya çevirelim
        price_cleaned = price.replace('£', '').replace(',', '').strip()
        
        # Fiyatı sayıya dönüştürelim (işlem sırasında hata alırsak kontrol ederiz)
        try:
            price_float = float(price_cleaned)
            book_prices.append(price_float)
        except ValueError:
            print(f"Fiyat dönüştürme hatası: {price_cleaned}")
            book_prices.append(None)  # Hatalı fiyatları None ile işaretleyebiliriz
    else:
        book_prices.append(None)  # Eğer fiyat bulunamadıysa None ekleyelim

# Fiyatlar ve başlıkları yazdıralım
print("\nKitaplar ve Fiyatları:")
for title, price in zip(book_titles, book_prices):
    print(f"{title}: {price}")

# DataFrame oluşturuluyor
import pandas as pd
data = {'Title': book_titles, 'Price': book_prices}
df = pd.DataFrame(data)

# Veriyi CSV dosyasına kaydedelim
df.to_csv('books_data.csv', index=False)
print("\nVeri 'books_data.csv' dosyasına kaydedildi.")
