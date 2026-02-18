from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'product-service',
        'timestamp': datetime.utcnow().isoformat()
    }), 200

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify({
        'message': 'Product service is running',
        'endpoint': '/api/products'
    }), 200

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    return jsonify({
        'message': 'Product service is running',
        'endpoint': f'/api/products/{product_id}',
        'product_id': product_id
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
