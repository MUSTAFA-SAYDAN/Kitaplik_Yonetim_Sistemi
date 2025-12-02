from flask import Blueprint, request, jsonify, current_app
from auth.services import kullanici_kaydet, kullanici_dogrula
from auth.validators import eksik_alan_kontrol
from models import Kullanici
import jwt
import datetime