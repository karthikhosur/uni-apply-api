from flask import Flask, request, jsonify
from evaluation import university_evaluation 

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
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
    if score>99:
        score = 20
            
    return jsonify({
        'Prediction': score
    })

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"



if __name__ == '__main__':
    app.run(threaded=True, port=5000)