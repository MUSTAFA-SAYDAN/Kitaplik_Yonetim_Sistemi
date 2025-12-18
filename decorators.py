from functools import wraps
from flask import request,jsonify,current_app
import jwt


def token_dogrula(f):
    @wraps(f)
    def sarici(*args,**kwargs):
        auth_header=request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"hata":"Token bulunamadı"}),401

        token=auth_header.split(" ")[1]

        try:
            data=jwt.decode(
                token,
                current_app.config["SECRET_KEY"],
                algorithms=["HS256"]
            )

            kullanici_id=data.get("kullanici_id")
            if not kullanici_id:
                return jsonify({"hata":"Token içeriği hatalı"}),401

            request.kullanici_id=kullanici_id

        except jwt.ExpiredSignatureError:
            return jsonify({"hata":"Token süresi dolmuş"}),401
        except jwt.InvalidTokenError:
            return jsonify({"hata":"Geçersiz token"}),401

        return f(*args,**kwargs)

    return sarici
