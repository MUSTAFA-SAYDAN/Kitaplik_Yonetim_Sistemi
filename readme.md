Kitaplık Yönetim Sistemi API
Bu proje, kullanıcıların hesap açıp giriş yapabileceği ve kitap ekleyip, listeleyip, güncelleyip, silebileceği basit bir RESTful API'dir. Flask, SQLite ve JWT kullanılarak geliştirilmiştir.

Özellikler
Kullanıcı kayıt ve giriş işlemleri (JWT ile güvenli kimlik doğrulama)

Kitap CRUD işlemleri (Ekleme, Listeleme, Güncelleme, Silme)

Token tabanlı yetkilendirme ile güvenlik

Kurulum
Projeyi klonlayın:

bash
Kopyala
Düzenle
git clone https://github.com/MUSTAFA-SAYDAN/kitaplik_yonetim_sistemi.git
cd kitaplik_yonetim_sistemi
Sanal ortam oluşturun ve aktif edin:

bash
Kopyala
Düzenle
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
Gerekli paketleri yükleyin:

bash
Kopyala
Düzenle
pip install -r requirements.txt
Uygulamayı başlatın:

bash
Kopyala
Düzenle
python app.py
API Kullanımı
Kullanıcı Kaydı
Endpoint: /kayit

Metod: POST

Gönderilecek JSON:

json
Kopyala
Düzenle
{
  "kullanici_adi": "Mustafa",
  "sifre": "1234"
}
Kullanıcı Girişi
Endpoint: /giris

Metod: POST

Gönderilecek JSON:

json
Kopyala
Düzenle
{
  "kullanici_adi": "Mustafa",
  "sifre": "1234"
}
Başarılı girişte JWT token döner.

Kitap Ekleme
Endpoint: /kitaplar

Metod: POST

Header: Authorization: Bearer <token>

Gönderilecek JSON:

json
Kopyala
Düzenle
{
  "isim": "Sefiller",
  "yazar": "Victor Hugo",
  "yayin_yili": 1862
}
Kitapları Listeleme
Endpoint: /kitaplar

Metod: GET

Tek Kitap Getirme
Endpoint: /kitaplar/<id>

Metod: GET

Kitap Güncelleme
Endpoint: /kitaplar/<id>

Metod: PUT

Header: Authorization: Bearer <token>

Gönderilecek JSON (örnek):

json
Kopyala
Düzenle
{
  "isim": "Sefiller - Güncellenmiş",
  "yayin_yili": 1863
}
Kitap Silme
Endpoint: /kitaplar/<id>

Metod: DELETE

Header: Authorization: Bearer <token>

Lisans
MIT Lisansı © 2025