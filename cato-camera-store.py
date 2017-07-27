from flask import Flask, request, send_file, make_response
from flask_restful import Api, Resource, abort
import os.path

app = Flask(__name__)
# removes standard 404 flask message
app.config["ERROR_404_HELP"]=False
api = Api(app)

class MovementImage(Resource):
    def post(self, fname):
        file = request.files['media']
        if file:
            filename = fname + '.jpg'
            file.save(filename)
            msg = "/movement/" + filename
            return msg, 201

        abort(400, message = "No file supplied")

    def get(self, fname):
        filename = fname + '.jpg'
        if os.path.isfile(filename):
            return send_file(filename, mimetype='image/jpeg')
        else:
            abort(404, message = "File not found")

api.add_resource(MovementImage, '/movement/<string:fname>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)