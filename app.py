from flask import Flask, render_template 
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('resume.html')

@app.route("/profile")
def profile():
	return render_template("finalProject.html")

@app.route('/hassan')
def hassan():
	return render_template('example.html')

@app.route('/goo')
def goo():
	return render_template('goo.html')

@app.route('/facebook')
def facebook():
	return render_template('facebook.html')

@app.route('/portfolio')
def portfolio():
	return render_template('portfolio.html')
	
if __name__ == "__main__":
    app.run()


