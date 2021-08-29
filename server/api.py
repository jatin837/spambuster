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
        text = args['text']
        spam_percentage = self.classify(text)
        return spam_percentage, 201

    def classify(self, text):
        return 0.5 

api.add_resource(Greet, '/')
api.add_resource(TextHandler, '/text')

if __name__ == '__main__':
    print("run ./serv in the root of project")
