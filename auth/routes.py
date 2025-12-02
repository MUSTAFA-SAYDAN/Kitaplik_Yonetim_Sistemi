from flask import Blueprint, request, jsonify, current_app
from auth.services import kullanici_kaydet, kullanici_dogrula
from auth.validators import eksik_alan_kontrol
from models import Kullanici
import jwt
import datetime

auth_bp=Blueprint("auth",__name__)

@auth_bp.route("/kayit",methods=["POST"])
def kayit():
    veri=request.get_json()
    eksik=eksik_alan_kontrol(veri,["kullanici_adi","sifre"])
    if eksik:
        return jsonify({"hata":f"{eksik} alanı eksik"}),400
    
    if Kullanici.query.filter_by(kullanici_adi=veri["kullanici_adi"]).first():
        return jsonify({"hata":"Kullanıcı zaten kayıtlı"}),400
    
    kullanici_kaydet(veri["kullanici_adi"],veri["sifre"])

    return jsonify({"mesaj":"Kayıt başarılı"}),201