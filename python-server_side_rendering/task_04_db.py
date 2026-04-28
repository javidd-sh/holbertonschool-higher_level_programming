import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# --- Helper functions ---
def get_json_data():
    with open('products.json', 'r') as f:
        return json.load(f)

def get_csv_data():
    data = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            data.append(row)
    return data

def get_sql_data():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    data = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return data

# --- Route ---
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Validation
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # Fetch based on source
    try:
        if source == 'json': all_data = get_json_data()
        elif source == 'csv': all_data = get_csv_data()
        elif source == 'sql': all_data = get_sql_data()
    except Exception as e:
        return render_template('product_display.html', error=f"Data error: {str(e)}")

    # Filtering
    if product_id:
        filtered = [p for p in all_data if str(p['id']) == product_id]
        if not filtered:
            return render_template('product_display.html', error="Product not found")
        return render_template('product_display.html', products=filtered)
    
    return render_template('product_display.html', products=all_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)