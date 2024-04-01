from flask import Flask, jsonify, request  # Import
from flask_cors import CORS  # CORS

app = Flask(__name__)  # Flask application instance
CORS(app)  # Allow CORS

products = [  # sample products
    {"id": 1, "name": "Product 1", "description": "Description 1"},
    {"id": 2, "name": "Product 2", "description": "Description 2"}
]

@app.route('/products', methods=['GET', 'POST'])  # Handling GET and POST products requests
def handle_products():
    if request.method == 'GET':
        return jsonify(products)  # Return the list of products
    if request.method == 'POST':
        product = request.json  # Extract JSON data from the request
        product["id"] = len(products) + 1  # unique ID to the new product
        products.append(product)  # Add the new product
        return jsonify(product), 201  # Return New created product

@app.route('/products/<int:id>', methods=['GET', 'PUT', 'DELETE'])  # Handling GET, PUT, and DELETE products requests
def handle_product(id):
    product = next((p for p in products if p['id'] == id), None)  # Find the product with ID
    if not product:  # If product is not found
        return jsonify({"message": "Product not found"}), 404  # Return error message
    
    if request.method == 'GET':
        return jsonify(product)  # Return the product details
    elif request.method == 'PUT':
        product.update(request.json)  # Update the product details
        return jsonify(product)  # Return the updated product details
    elif request.method == 'DELETE':
        products.remove(product)  # Remove the product from the list of products
        return '', 204  # Return the product deletion

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode
