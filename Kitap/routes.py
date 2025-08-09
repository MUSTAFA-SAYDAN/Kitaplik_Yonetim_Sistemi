from flask import Blueprint, request, jsonify
from Kitap.services import kitap_ekle, kitap_getir, kitap_guncelle, kitap_sil
from Kitap.validators import eksik_alan_kontrol
from decorators import token_dogrula
from models import Kitap

kitap_bp = Blueprint("kitaplar", __name__)

@kitap_bp.route("/", methods=["POST"])
@token_dogrula
def kitap_ekle_route():
    veri = request.get_json()
    eksik = eksik_alan_kontrol(veri, ["isim", "yazar", "yayin_yili"])
    if eksik:
        return jsonify({"hata": f"{eksik} alanı eksik"}), 400

    yeni_kitap = kitap_ekle(
        veri["isim"],
        veri["yazar"],
        veri["yayin_yili"],
        request.kullanici_id
    )
    return jsonify({"mesaj": "Kitap eklendi", "kitap_id": yeni_kitap.id}), 201

@kitap_bp.route("/", methods=["GET"])
@token_dogrula
def kitaplari_getir():
    kitaplar = Kitap.query.filter_by(kullanici_id=request.kullanici_id).all()
    sonuc = [k.to_dict() for k in kitaplar]
    return jsonify(sonuc), 200

@kitap_bp.route("/<int:kitap_id>", methods=["GET"])
@token_dogrula
def kitap_getir_route(kitap_id):
    kitap = Kitap.query.filter_by(id=kitap_id, kullanici_id=request.kullanici_id).first_or_404()
    return jsonify(kitap.to_dict()), 200

@kitap_bp.route("/<int:kitap_id>", methods=["PUT"])
@token_dogrula
def kitap_guncelle_route(kitap_id):
    veri = request.get_json()
    kitap = Kitap.query.filter_by(id=kitap_id, kullanici_id=request.kullanici_id).first_or_404()
    kitap_guncelle(
        kitap,
        veri.get("isim"),
        veri.get("yazar"),
        veri.get("yayin_yili")
    )
    return jsonify({"mesaj": "Kitap güncellendi"}), 200

@kitap_bp.route("/<int:kitap_id>", methods=["DELETE"])
@token_dogrula
def kitap_sil_route(kitap_id):
    kitap = Kitap.query.filter_by(id=kitap_id, kullanici_id=request.kullanici_id).first_or_404()
    kitap_sil(kitap)
    return jsonify({"mesaj": "Kitap silindi"}), 200
