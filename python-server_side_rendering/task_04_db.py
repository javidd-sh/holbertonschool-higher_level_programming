import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def get_db_data(product_id=None):
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name
    cursor = conn.cursor()
    
    if product_id:
        cursor.execute("SELECT * FROM Products WHERE id = ?", (product_id,))
    else:
        cursor.execute("SELECT * FROM Products")
        
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # 1. Validate Source
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # 2. Fetch Data Based on Source
    try:
        if source == 'sql':
            all_data = get_db_data()
        else:
            # Re-use your existing json/csv logic here
            all_data = get_data_from_files(source) 
    except Exception as e:
        return render_template('product_display.html', error=f"Database error: {str(e)}")

    # 3. Filter by ID if provided
    if product_id:
        filtered = [p for p in all_data if str(p['id']) == product_id]
        if not filtered:
            return render_template('product_display.html', error="Product not found")
        return render_template('product_display.html', products=filtered)
    
    return render_template('product_display.html', products=all_data)