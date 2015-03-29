from flask import Flask, render_template, url_for
from test import getTemp
app = Flask(__name__)

@app.route("/")
def coophome():
	temp = str(getTemp())
	return render_template('main.html', temp=temp)

if __name__ == "__main__":
	app.run(debug=True)
