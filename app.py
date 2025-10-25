from flask import Flask, render_template

app = Flask(__name__)

# -----------------------
# Routes
# -----------------------

@app.route('/')
def portfolio():
    return render_template("home.html")

@app.route('/projects')
def projects():
    return render_template("project.html")

@app.route('/education')
def education():
    return render_template("education.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


# -----------------------
# Entry Point
# -----------------------
if __name__ == '__main__':
    app.run(debug=True)
