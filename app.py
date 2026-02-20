from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Jenkins!"

@app.route('/add/<path:values>')
def add(values):
    try:
        a, b = map(int, values.split('/'))
        return str(a + b)
    except:
        return "Invalid input", 400

if __name__ == '__main__':
    app.run(debug=True)
