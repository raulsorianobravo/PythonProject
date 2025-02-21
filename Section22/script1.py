from flask import Flask

# Constructor
# Scrip Executed __name__ = __main__
# Scriptp Imported __name__ = "filename"
app = Flask(__name__)

# root of the website
@app.route('/')

def home():
    return "Home Page"

@app.route('/about/')

def about():
    return "Website Content"

# Debug mode
if __name__ == "__main__":
    app.run(debug=True)