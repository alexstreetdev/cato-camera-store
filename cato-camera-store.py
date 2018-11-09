from flask import Flask, request, send_file, make_response
from flask_restful import Api, Resource, abort
import os.path
import sys

app = Flask(__name__)
# removes standard 404 flask message
app.config["ERROR_404_HELP"]=False
app.config["UPLOAD_FOLDER"]="/app/cato-camera-store"
api = Api(app)

class MovementImage(Resource):
    def post(self, fname):
        file = request.files['media']
        if file:
            fpath = os.path.join(app.config['UPLOAD_FOLDER'],app.config['FILEPATH'], fname)
            print(fpath)
            file.save(fpath)
            msg = "/movement/" + fname + ":" + fpath
            return msg, 201

        abort(400, message = "No file supplied")

    def get(self, fname):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], fname)
        if os.path.isfile(filename):
            return send_file(filename, mimetype='image/jpeg')
        else:
            abort(404, message = "File not found")

api.add_resource(MovementImage, '/movement/<string:fname>')

if __name__ == '__main__':
	app.config['FILEPATH']=sys.argv[1]
    app.run(host="0.0.0.0", port=5001)
