# colmapで生成したデータを読み込む & その他2D, 3Dデータの配置を行うページ
# 3Dモデルの読み込み用ボタン : ply読み込み→ply2objが走る→モデルが展開される
# 2D画像の読み込み用ボタン : 読み込み→展開
# +α colmap由来以外のの3Dモデルを読み込み→展開

#plyじゃないとエラーになるようにする
import os
from flask import(
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename

bp = Blueprint("expand", __name__, url_prefix = "/expand")

@bp.route("/")
def index():
    return render_template("expand/index.html")

#不要かもしれない
@bp.route("/upload_plyfile")
def upload_plyfile():
    return render_template("expand/upload.html")



# ファイル入力後に関数に進む場合, methods=["POST"]がないとエラー
@bp.route("/savefile", methods=["POST"])
def savefile():
    os.makedirs('upload_folder/', exist_ok=True)
    if request.method == 'POST':
        files = request.files.getlist('file')
        # ここはplyファイル用なので, 複数ファイルの必要はない. あとで plyかの判定を追加
        for file in files:
            file.save(os.path.join('upload_folder/',secure_filename(file.filename)))
            
        return render_template("expand/index.html")