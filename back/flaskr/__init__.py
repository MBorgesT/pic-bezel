import os
from flask import Flask, request, send_file
from flaskr.bezel import make_bezel


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        #DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        #UPLOAD_FOLDER='/home/matheus/Code/pic-bezel/flaskr/files/'
        UPLOAD_FOLDER=os.path.join(app.instance_path, 'files/')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/bezel', methods=['POST'])
    def upload():
        imagefile = request.files.get('image')
        zip_path = make_bezel(imagefile, app.config['UPLOAD_FOLDER'])
        return send_file(zip_path)
        

    return app