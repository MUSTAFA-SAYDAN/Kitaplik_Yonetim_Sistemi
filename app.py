from flask import Flask
from extensions import db,bcrypt,migrate
from Kitap.routes import kitap_bp
from auth.routes import auth_bp


def create_app():
    app=Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///veritabani.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    app.config["SECRET_KEY"]="gizli_anahtar"

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(auth_bp,url_prefix="/auth")
    app.register_blueprint(kitap_bp,url_prefix="/kitaplar")

    return app


if __name__ == "__main__":
    app=create_app()
    app.run(debug=True,port=5001)
    