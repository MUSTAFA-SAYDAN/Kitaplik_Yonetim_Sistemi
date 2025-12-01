from extensions import db,bcrypt

class Kullanici(db.Model):
    __tablename__="kullanicilar"

    id=db.Column(db.Integer,primary_key=True)
    kullanici_adi=db.Column(db.String(100),unique=True,nullable= False)
    sifre_hash=db.Column(db.String(150),nullable=False)

    kitaplar=db.relationship("Kitap",backref="kullanici",lazy=True)

    def sifre_kontrol(self,sifre):
        return bcrypt.check_password_hash(self.sifre_hash,sifre)
    

class Kitap(db.Model):
    __tablename__="kitaplar"

    id=db.Column(db.Integer,primary_key=True)
    isim=db.Column(db.String(100),nullable=False)
    yazar=db.Column(db.String(100),nullable=False)
    sayfa_sayisi=db.Column(db.Integer,nullable=False)
    kategori=db.Column(db.String(100),nullable=False)
    yayin_yili = db.Column(db.Integer, nullable=False)
    yayinevi=db.Column(db.String(100),nullable=False)
    okundu_mu=db.Column(db.Boolean,default=False,nullable=False)

    kullanici_id=db.Column(db.Integer,db.ForeignKey("kullanicilar.id"),nullable=False)

    def to_dict(self):
        return{
            "id":self.id,
            "isim":self.isim,
            "yazar":self.yazar,
            "sayfa_sayisi":self.sayfa_sayisi,
            "kategori":self.kategori,
            "yayin_yili":self.yayin_yili,
            "yayinevi":self.yayinevi,
            "okundu_mu":self.okundu_mu,
            "kullanici_id":self.kullanici_id
        }