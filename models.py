from extensions import db,bcrypt
from datetime import datetime

class Kullanici(db.Model):
    __tablename__="kullanicilar"

    id=db.Column(db.Integer,primary_key=True)
    kullanici_adi=db.Column(db.String(100),unique=True,nullable= False)
    sifre_hash=db.Column(db.String(100),nullable=False)

    kitaplar=db.relationship("Kitap",backref="kullanici",lazy=True)

    def sifre_kontrol(self,sifre):
        return bcrypt.check_password_hash(self.sifre_hash,sifre)
    




