from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        name = request.form.get('StudentName')
        sid = request.form.get('StudentID')
        return render_template("result.html", name=name, sid=sid)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

