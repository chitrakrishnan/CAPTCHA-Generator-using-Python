from flask import Flask,render_template

app = flask(__name__)
@app.route('/')
def index():
    return render_template('form.html')

if__name__ == "__main__":
app.run(debug=True)    