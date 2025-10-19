import sys
import os

# Adiciona a pasta raiz do projeto ao path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(BASE_DIR)

from flask import Flask, request, jsonify
from flask_cors import CORS
from api.config import Config
from db.models import db, Recommendation
from ai.ia_model import generate_recommendations

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db.init_app(app)

@app.route('/')
def home():
    return jsonify({'message': 'OrientAI API funcionando!'})

@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    user_input = data.get('answers', '')

    recommendations = generate_recommendations(user_input)

    # rec = Recommendation(user_input=user_input, recommended_courses=", ".join(recommendations))
    rec = Recommendation(course=", ".join(recommendations))
    db.session.add(rec)
    db.session.commit()

    return jsonify({'recommendations': recommendations})

@app.route('/api/history', methods=['GET'])
def history():
    all_rec = Recommendation.query.all()
    results = [{'id': r.id, 'course': r.course} for r in all_rec]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)