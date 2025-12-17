from extensions import db
from models import Kitap

def kitap_ekle(isim,yazar,sayfa_sayisi,kategori,yayin_yili,yayinevi,okundu_mu,kullanici_id):
    yeni_kitap=Kitap(
        isim=isim,
        yazar=yazar,
        sayfa_sayisi=sayfa_sayisi,
        kategori=kategori,
        yayin_yili=yayin_yili,
        yayinevi=yayinevi,
        okundu_mu=okundu_mu,
        kullanici_id=kullanici_id
    )

    db.session.add(yeni_kitap)
    db.session.commit()

    return yeni_kitap


def kitap_getir(kitap_id,kullanici_id):
    kitap=Kitap.query.filter_by(id=kitap_id,kullanici_id=kullanici_id).first()

    return kitap


def kitap_guncelle(kitap_id,isim,yazar,sayfa_sayisi,kategori,yayin_yili,yayinevi,okundu_mu,kullanici_id):
    kitap = Kitap.query.filter_by(id=kitap_id,kullanici_id=kullanici_id).first()
    if not kitap:
        return None

    kitap.isim=isim
    kitap.yazar=yazar
    kitap.sayfa_sayisi=sayfa_sayisi
    kitap.kategori=kategori
    kitap.yayin_yili=yayin_yili
    kitap.yayinevi=yayinevi
    kitap.okundu_mu=okundu_mu

    db.session.commit()

    return kitap
