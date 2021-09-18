from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from lib.classifier import Text

app = Flask(__name__)
api = Api(app)

####parser = reqparse.RequestParser()
####parser.add_argument('text', type=str, help = 'give me a string of text')

class Greet(Resource):
    def get(self):
        return {'msg': 'hi'}

class TextHandler(Resource):
    def post(self):
       #args = parser.parse_args()
       #text = Text(args['text'])
       #spam_percentage = self.classify(text)
        data = request.get_json(force=True)
        text = data['text']
        spam_percentage = self.classify(text)
        return jsonify(val=spam_percentage)

    def classify(self, text):
        textObj = Text(text)
        return textObj.get_spam_percentage() 

api.add_resource(Greet, '/')
api.add_resource(TextHandler, '/text')

if __name__ == '__main__':
    print("run ./serv in the root of project")
