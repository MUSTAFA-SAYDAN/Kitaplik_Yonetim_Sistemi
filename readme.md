# 📚 Kitaplık Yönetim Sistemi API

Bu proje, kullanıcıların kitap ekleyip, listeleyebileceği, güncelleyebileceği ve silebileceği basit bir RESTful API'dir. Flask, SQLAlchemy, Flask-Bcrypt ve JWT teknolojileri kullanılarak geliştirilmiştir.

## Özellikler

- Kullanıcı kayıt ve giriş işlemleri (JWT ile kimlik doğrulama)
- Kitap CRUD (Oluşturma, Okuma, Güncelleme, Silme) işlemleri
- Token tabanlı yetkilendirme ile güvenlik

## Kurulum

1. Projeyi klonlayın:

```bash
git clone https://github.com/MUSTAFA-SAYDAN/kitaplik_yonetim_sistemi.git
cd kitaplik_yonetim_sistemi
Sanal ortam oluşturun ve aktif edin:

bash
Kopyala
Düzenle
python -m venv venv

# Windows için
venv\Scripts\activate

# Linux/Mac için
source venv/bin/activate
Gerekli kütüphaneleri yükleyin:

bash
Kopyala
Düzenle
pip install -r requirements.txt
Veritabanını oluşturun (ilk çalıştırmada otomatik oluşur):

bash
Kopyala
Düzenle
python app.py
API Kullanımı
✅ Kullanıcı Kaydı
Endpoint: /kayit

Metod: POST

json
Kopyala
Düzenle
{
  "kullanici_adi": "Mustafa",
  "sifre": "1234"
}
🔐 Giriş Yap
Endpoint: /giris

Metod: POST

json
Kopyala
Düzenle
{
  "kullanici_adi": "Mustafa",
  "sifre": "1234"
}
Başarılı girişte JWT token döner.

➕ Kitap Ekle
Endpoint: /kitaplar

Metod: POST

Header: Authorization: Bearer <token>

json
Kopyala
Düzenle
{
  "isim": "1984",
  "yazar": "George Orwell",
  "yayin_yili": 1949
}
📄 Kitapları Listele
Endpoint: /kitaplar

Metod: GET

📘 Kitap Detayı Getir
Endpoint: /kitaplar/<id>

Metod: GET

✏️ Kitap Güncelle
Endpoint: /kitaplar/<id>

Metod: PUT

Header: Authorization: Bearer <token>

json
Kopyala
Düzenle
{
  "isim": "Hayvan Çiftliği",
  "yazar": "George Orwell",
  "yayin_yili": 1945
}
❌ Kitap Sil
Endpoint: /kitaplar/<id>

Metod: DELETE

Header: Authorization: Bearer <token>

Lisans
MIT Lisansı © 2025
