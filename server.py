from flask import Flask, render_template
import json

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    site_key = ""
    return render_template('render.html', site_key=site_key)

if __name__ == '__main__':
    app.run(debug=True, port=80)
