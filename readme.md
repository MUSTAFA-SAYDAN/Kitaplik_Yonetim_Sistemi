📚 Kitaplık Yönetim Sistemi API

Bu proje, kullanıcıların kitap ekleyip, listeleyebileceği, güncelleyebileceği ve silebileceği basit bir RESTful API'dir. Flask, SQLAlchemy, Flask-Bcrypt ve JWT teknolojileri kullanılarak geliştirilmiştir.

🚀 Özellikler
Kullanıcı kayıt ve giriş işlemleri (JWT ile kimlik doğrulama)

Kitap CRUD (Oluşturma, Okuma, Güncelleme, Silme) işlemleri

Token tabanlı yetkilendirme ile güvenlik

⚙️ Kurulum
1. Projeyi klonlayın:
bash
Kopyala
Düzenle
git clone https://github.com/MUSTAFA-SAYDAN/kitaplik_yonetim_sistemi.git
cd kitaplik_yonetim_sistemi
2. Sanal ortam oluşturun ve aktif edin:
bash
Kopyala
Düzenle
python -m venv venv
venv\Scripts\activate
3. Gerekli paketleri yükleyin:
bash
Kopyala
Düzenle
pip install -r requirements.txt
4. Uygulamayı çalıştırın:
bash
Kopyala
Düzenle
python app.py
📬 API Kullanımı
✅ Kullanıcı Kaydı
Endpoint: /kayit

Metod: POST

JSON Gönderimi:

json
Kopyala
Düzenle
{
  "kullanici_adi": "ali",
  "sifre": "1234"
}
🔐 Kullanıcı Girişi
Endpoint: /giris

Metod: POST

JSON Gönderimi:

json
Kopyala
Düzenle
{
  "kullanici_adi": "ali",
  "sifre": "1234"
}
Başarılı girişte JWT token döner.

➕ Kitap Ekleme
Endpoint: /kitaplar

Metod: POST

Header: Authorization: Bearer <token>

JSON Gönderimi:

json
Kopyala
Düzenle
{
  "isim": "1984",
  "yazar": "George Orwell",
  "yayin_yili": 1949
}
📄 Kitapları Listeleme
Endpoint: /kitaplar

Metod: GET

📘 Tek Kitap Getirme
Endpoint: /kitaplar/<id>

Metod: GET

✏️ Kitap Güncelleme
Endpoint: /kitaplar/<id>

Metod: PUT

Header: Authorization: Bearer <token>

JSON Gönderimi:

json
Kopyala
Düzenle
{
  "isim": "Hayvan Çiftliği",
  "yazar": "George Orwell"
}
❌ Kitap Silme
Endpoint: /kitaplar/<id>

Metod: DELETE

Header: Authorization: Bearer <token>

📄 Lisans
MIT Lisansı © 2025
