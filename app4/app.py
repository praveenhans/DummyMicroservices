import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<body style='background-color:powderblue;'><h1>Sample Application for microservices</h1><p>This site is a prototype API for app4.</p>"

app.run(port=5000, debug=True, host="0.0.0.0")