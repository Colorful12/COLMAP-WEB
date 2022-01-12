# colmapで生成したデータを読み込む & その他2D, 3Dデータの配置を行うページ

from flask import(
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

bp = Blueprint("expand", __name__, url_prefix = "/expand")

@bp.route("/")
def index():
    return render_template("expand/index.html")