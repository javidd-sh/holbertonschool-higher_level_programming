import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def get_data(source):
    data = []
    if source == 'json':
        with open('products.json', 'r') as f:
            data = json.load(f)
    elif source == 'csv':
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert numeric types
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
    return data

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    all_data = get_data(source)
    
    if product_id:
        filtered = [p for p in all_data if p['id'] == int(product_id)]
        if not filtered:
            return render_template('product_display.html', error="Product not found")
        return render_template('product_display.html', products=filtered)
    
    return render_template('product_display.html', products=all_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)