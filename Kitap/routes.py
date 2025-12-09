from flask import Blueprint,request,jsonify
from decorators import token_dogrula
from Kitap.services import kitap_ekle,kitap_getir,kitap_guncelle,kitap_sil
from Kitap.validators import eksik_alan_kontrol
from models import Kitap

kitap_bp=Blueprint("kitaplar",__name__)

@kitap_bp.route("/",methods=["POST"])
@token_dogrula
def kitap_ekle_route():
    veri=request.get_json()
    eksik=eksik_alan_kontrol(veri,["isim","yazar","sayfa_sayisi","kategori","yayin_yili","yayinevi","okundu_mu"])
    if eksik:
        return jsonify({"hata":f"{eksik} alanı eksik"}), 400
    
    yeni_kitap=kitap_ekle(
        veri["isim"],
        veri["yazar"],
        veri["sayfa_sayisi"],
        veri["kategori"],
        veri["yayin_yili"],
        veri["yayinevi"],
        veri["okundu_mu"],
        request.kullanici_id
    )
    return jsonify({"mesaj":"Kitap eklendi","kitap_id":yeni_kitap.id}), 201