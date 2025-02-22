from flask import Flask, render_template


# Constructor
# Scrip Executed __name__ = __main__
# Scriptp Imported __name__ = "filename"
app = Flask(__name__)

# root of the website
@app.route('/')

def home():
    return render_template("home.html")

@app.route('/about/')

def about():
    return "Website Content"

# Debug mode
if __name__ == "__main__":
    app.run(debug=True)