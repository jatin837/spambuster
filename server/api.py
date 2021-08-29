from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('text', type=str, help = 'give me a string of text')

class Greet(Resource):
    def get(self):
        return {'msg': 'hi'}

class TextHandler(Resource):
    def post(self):
        args = parser.parse_args()
        return "I promise to determine if this is a spam or ham", 201
    

api.add_resource(Greet, '/')
api.add_resource(TextHandler, '/text')

if __name__ == '__main__':
    print("run ./serv in the root of project")