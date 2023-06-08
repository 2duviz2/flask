from flask import Flask

app = Flask(__name__)

@app.route("/encontrar")
def about():
    return '<h1>Tengo una buena idea para encontrar a zapatos no me sigais...</h1>'

@app.route("/xd")
def xd():
    return '<h1>https://www.youtube.com/watch?v=dQw4w9WgXcQ <- que sera eso?</h1>'

@app.route("/")
def index():
    return '<h1>Zapatos una cosita!</h1>'


app.run(debug=True)
