from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from evaluation import university_evaluation 


app = Flask(__name__)
api = Api(app)


class MakePrediction(Resource):
    @staticmethod
    def post():
        posted_data = request.get_json()
        gre = posted_data['gre']
        toefl = posted_data['toefl']
        uni_rate = posted_data['uni_rate']
        sop_rate = posted_data['sop_rate']
        lor_rate = posted_data['lor_rate']
        cgpa = posted_data['cgpa']
        research = posted_data['research']
   
        score = university_evaluation(gre, toefl, uni_rate, sop_rate, lor_rate, cgpa, research)
        if score>99 or score<10:
            score = 90
            
        return jsonify({
            'Prediction': score
        })


api.add_resource(MakePrediction, '/predict')


if __name__ == '__main__':
    app.run() 