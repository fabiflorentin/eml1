from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# load trainned model generated in notebook
with open('modelo.pkl', 'rb') as arquivo:
    modelo = pickle.load(arquivo)

@app.route('/predict', methods=['GET'])
def predict():
    tv = int (request.args.get('tv_sub'))
    movie = int (request.args.get('movie_sub'))
    age = float (request.args.get('age'))
    hasContract = int (request.args.get('has_contract'))
    
    data = np.array([[tv,movie,age,hasContract]])

    churn = modelo.predict(data)

    return jsonify({'churn': int(churn[0])})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


