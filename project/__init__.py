# projectの実体

import os
from flask import Flask, render_template,request
from werkzeug.utils import secure_filename #

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    UPLOAD_FOLDER = 'upload_folder/'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    @app.route("/")
    def root():
        return render_template("base.html")

    @app.route('/upload')
    def upload():
        return render_template('upload.html')

    @app.route('/upload_file',methods=['POST'])
    def upload_file():
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        if request.method == 'POST':
            files = request.files.getlist('file')
            for file in files:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
            return 'file uploaded successfully'
    

    from . import expand
    app.register_blueprint(expand.bp)

    return app