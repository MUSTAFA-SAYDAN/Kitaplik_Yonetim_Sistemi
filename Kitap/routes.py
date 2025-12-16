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


@kitap_bp.route("/",methods=["GET"])
@token_dogrula
def kitap_listele_route():
    kitaplar=Kitap.query.filter_by(kullanici_id=request.kullanici_id).all()

    liste=[]
    for k in kitaplar:
        liste.append(
            {
            "id":k.id,
            "isim":k.isim,
            "yazar":k.yazar,
            "sayfa_sayisi":k.sayfa_sayisi,
            "kategori":k.kategori,
            "yayin_yili":k.yayin_yili,
            "yayinevi":k.yayinevi,
            "okundu_mu":k.okundu_mu
        }
        )

    return jsonify(liste),200


@kitap_bp.route("/<int:id>",methods=["GET"])
@token_dogrula
def kitap_getir_route(id):
    kitap=kitap_getir(id,request.kullanici_id)
    if not kitap:
        return jsonify({"hata":"Kitap bulunamadı"}),404

    return jsonify({
        "id":kitap.id,
        "isim":kitap.isim,
        "yazar":kitap.yazar,
        "sayfa_sayisi":kitap.sayfa_sayisi,
        "kategori":kitap.kategori,
        "yayin_yili":kitap.yayin_yili,
        "yayinevi":kitap.yayinevi,
        "okundu_mu":kitap.okundu_mu
    }),200


@kitap_bp.route("/<int:id>", methods=["PUT"])
@token_dogrula
def kitap_guncelle_route(id):
    veri = request.get_json()

    eksik = eksik_alan_kontrol(veri, ["isim","yazar","sayfa_sayisi","kategori","yayin_yili","yayinevi","okundu_mu"])
    if eksik:
        return jsonify({"hata":f"{eksik} alanı eksik"}),400

    guncel_kitap=kitap_guncelle(
        id,
        veri["isim"],
        veri["yazar"],
        veri["sayfa_sayisi"],
        veri["kategori"],
        veri["yayin_yili"],
        veri["yayinevi"],
        veri["okundu_mu"],
        request.kullanici_id
    )

    if not guncel_kitap:
        return jsonify({"hata":"Kitap bulunamadı veya yetkiniz yok"}),404

    return jsonify({"mesaj":"Kitap güncellendi"}),200


@kitap_bp.route("/<int:id>",methods=["DELETE"])
@token_dogrula
def kitap_sil_route(id):
    silindi=kitap_sil(id,request.kullanici_id)
    if not silindi:
        return jsonify({"hata":"Kitap bulunamadı veya yetkiniz yok"}),404

    return jsonify({"mesaj":"Kitap silindi"}),200

