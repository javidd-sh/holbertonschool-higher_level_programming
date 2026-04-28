import json
from flask import Flask, render_template

app = Flask(__name__)

# ... (keep your existing routes)

@app.route('/items')
def items():
    # Load the JSON data
    with open('items.json', 'r') as f:
        data = json.load(f)
    
    # Pass the list of items to the template
    return render_template('items.html', items=data.get('items', []))