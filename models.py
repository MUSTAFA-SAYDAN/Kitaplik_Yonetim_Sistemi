from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class Kullanici(db.Model):
    __tablename__ = "kullanicilar"
    id = db.Column(db.Integer, primary_key=True)
    kullanici_adi = db.Column(db.String(50), unique=True, nullable=False)
    sifre_hash = db.Column(db.String(128), nullable=False)

    def sifre_kontrol(self, sifre):
        return bcrypt.check_password_hash(self.sifre_hash, sifre)

class Kitap(db.Model):
    __tablename__ = "kitaplar"
    id = db.Column(db.Integer, primary_key=True)
    isim = db.Column(db.String(100), nullable=False)
    yazar = db.Column(db.String(100), nullable=False)
    yayin_yili = db.Column(db.Integer, nullable=False)
    kullanici_id = db.Column(db.Integer, db.ForeignKey("kullanicilar.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "isim": self.isim,
            "yazar": self.yazar,
            "yayin_yili": self.yayin_yili
        }
