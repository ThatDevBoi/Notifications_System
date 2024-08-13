from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

latest_message = None

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/send-notification', methods=['POST'])
def send_notification():
    global latest_message
    data = request.get_json()
    latest_message = data.get('message')
    
    if latest_message:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False}), 400

@app.route('/get-notification', methods=['GET'])
def get_notification():
    global latest_message
    return jsonify({'message': latest_message})

if __name__ == '__main__':
    app.run(debug=True)
