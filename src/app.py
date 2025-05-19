from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Calculator API is running. Send a POST request to /calculate"

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    n1 = data.get('n1')
    n2 = data.get('n2')
    op = data.get('op')

    try:
        n1 = int(n1)
        n2 = int(n2)
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid numbers'}), 400

    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    elif op in ('*', 'x'):
        result = n1 * n2
    elif op == '/':
        if n2 == 0:
            return jsonify({'error': 'Division by zero'}), 400
        result = n1 / n2
    else:
        return jsonify({'error': 'Invalid operation'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
