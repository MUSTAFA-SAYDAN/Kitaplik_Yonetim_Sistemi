from models import Kitap
from extensions import db

def kitap_ekle(isim, yazar, yayin_yili, kullanici_id):
    yeni_kitap = Kitap(isim=isim, yazar=yazar, yayin_yili=yayin_yili, kullanici_id=kullanici_id)
    db.session.add(yeni_kitap)
    db.session.commit()
    return yeni_kitap

def kitap_getir(kitap_id):
    return Kitap.query.get_or_404(kitap_id)

def kitap_guncelle(kitap, isim=None, yazar=None, yayin_yili=None):
    if isim is not None:
        kitap.isim = isim
    if yazar is not None:
        kitap.yazar = yazar
    if yayin_yili is not None:
        kitap.yayin_yili = yayin_yili

    db.session.commit()
    return kitap

def kitap_sil(kitap):
    db.session.delete(kitap)
    db.session.commit()
