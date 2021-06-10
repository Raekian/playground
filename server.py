from flask import Flask, render_template  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/play')
def index():
    x = 3
    return render_template('index.html', x = x)

@app.route('/play/<int:number>')
def multiple(number):
    x = number
    return render_template('index.html', x = x)

@app.route('/play/<int:number>/<string:color>')
def color(number, color):
    x = number
    y = color
    return render_template('index.html', x = x, y = y)

if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
