import json
import os
from flask import Flask, render_template

app = Flask(__name__)

def load_items():
    if not os.path.exists('items.json'):
        return []
    with open('items.json', 'r') as f:
        try:
            data = json.load(f)
            return data.get('items', [])
        except json.JSONDecodeError:
            return []

@app.route('/items')
def items():
    item_list = load_items()
    return render_template('items.html', items=item_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)