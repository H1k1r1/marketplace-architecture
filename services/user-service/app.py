from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'user-service',
        'timestamp': datetime.utcnow().isoformat()
    }), 200

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({
        'message': 'User service is running',
        'endpoint': '/api/users'
    }), 200

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify({
        'message': 'User service is running',
        'endpoint': f'/api/users/{user_id}',
        'user_id': user_id
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
