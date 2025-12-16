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