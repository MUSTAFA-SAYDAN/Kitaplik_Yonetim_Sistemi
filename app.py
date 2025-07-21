from flask import Flask,request,jsonify
from models import db,bcrypt,Kullanici,Kitap
from functools import wraps
import jwt
import datetime

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///kitaplar.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SECRET_KEY"]="gizli_anahtar"

db.init_app(app)
bcrypt.init_app(app)

with app.app_context():
    db.create_all()


#----JWT------
def token_gerekli(f):
    @wraps(f)
    def sarici(*args,**kwargs):
        token=request.headers.get("Authorization")
        if not token:
            return jsonify({"hata":"Token gerekli!!!"}),401
        try:
            token=token.replace("Bearer ","")
            data=jwt.decode(token,app.config["SECRET_KEY"],algorithms=["HS256"])
            kullanici_id=data["kullanici_id"]
        except jwt.ExpiredSignatureError:
            return jsonify({"hata":"Token süresi dolmuş"}),401
        except jwt.InvalidTokenError:
            return jsonify({"hata":"Geçersiz token"}),401
        
        return f(kullanici_id,*args,**kwargs)
    return sarici


#--------KAYIT-------
@app.route("/kayit",methods=["POST"])
def kayit():
    data=request.json
    kullanici_adi=data.get("kullanici_adi")
    sifre=data.get("sifre")

    if Kullanici.query.filter_by(kullanici_adi=kullanici_adi).first():
        return jsonify({"hata":"Bu kullanici adi zaten alinmiş"}),400
    
    sifre_hash=bcrypt.generate_password_hash(sifre).decode("utf-8")
    yeni_kişi=Kullanici(kullanici_adi=kullanici_adi,sifre_hash=sifre_hash)
    db.session.add(yeni_kişi)
    db.session.commit()

    return jsonify({"mesaj":"Yeni kisi eklendi"}),201

#-------GİRİŞ---------
@app.route("/giris",methods=["POST"])
def giris():
    data=request.json
    kullanici_adi=data.get("kullanici_adi")
    sifre=data.get("sifre")

    kullanici=Kullanici.query.filter_by(kullanici_adi=kullanici_adi).first()
    if not kullanici or not kullanici.sifre_kontrol(sifre):
        return jsonify({"hata":"Kullanici adi veya sifre geçersiz"}),401
    
    token=jwt.encode(
        {
            "kullanici_id":kullanici.id,
            "exp":datetime.datetime.utcnow() +datetime.timedelta(hours=3)
        },
        app.config["SECRET_KEY"],
        algorithm="HS256"
    )

    return jsonify({"token":token})

#---------EKLEME----------
@app.route("/kitaplar",methods=["POST"])
@token_gerekli
def kitap_ekle(kullanici_id):
    data=request.json
    isim=data.get("isim")
    yazar=data.get("yazar")
    yayin_yili=data.get("yayin_yili")

    if not isim or not yazar or not yayin_yili:
        return jsonify({"hata":"Bilgiler eksik"}),400
    
    yeni_kitap=Kitap(isim=isim,yazar=yazar,yayin_yili=yayin_yili,kullanici_id=kullanici_id)
    db.session.add(yeni_kitap)
    db.session.commit()

    return jsonify({"mesaj":"Kitap eklendi"}),201

#----------TÜM KİTAPLARI LİSTELEME-----------
@app.route("/kitaplar",methods=["GET"])
def kitaplari_getir():
    kitaplar=Kitap.query.all()
    return jsonify([k.to_dict() for k in kitaplar])

#----------ID'YE GÖRE KİTAP GETİRME---------
@app.route("/kitaplar/<int:id>",methods=["GET"])
def kitabi_getir(id):
    kitap=Kitap.query.get(id)
    if not kitap:
        return jsonify({"hata":"Kitap bulunamadi"}),404
    return jsonify(kitap.to_dict())

#---------KİTAP GÜNCELLEME-----------
@app.route("/kitaplar/<int:id>",methods=["PUT"])
@token_gerekli
def kitap_guncelle(kullanici_id,id):
    kitap=Kitap.query.filter_by(id=id,kullanici_id=kullanici_id).first()
    if not kitap:
        return jsonify({"hata":"kitap bulunamadi"}),404
    
    data=request.json
    kitap.isim=data.get("isim",kitap.isim)
    kitap.yazar=data.get("yazar",kitap.yazar)
    kitap.yayin_yili=data.get("yayin_yili",kitap.yayin_yili)

    db.session.commit()

    return  jsonify({"mesaj":"Kitap güncellendi","kitap":kitap.to_dict()})

#------------KİTAP SİLME-----------
@app.route("/kitaplar/<int:id>",methods=["DELETE"])
@token_gerekli
def kitap_sil(kullanici_id,id):
    kitap=Kitap.query.filter_by(id=id,kullanici_id=kullanici_id).first()
    if not kitap:
        return jsonify({"hata":"kitap bulunamadi"}),404
    
    db.session.delete(kitap)
    db.session.commit()

    return jsonify({"mesaj":"Kitap silindi"})

if __name__=="__main__":
    app.run(debug=True,port=5001)

    



