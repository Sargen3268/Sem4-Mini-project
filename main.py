from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['user_text']

    # store the text in a file
    with open("data.txt", "a") as f:
        f.write(text + "\n")

    return "Wait patiently"

app.run(debug=True)