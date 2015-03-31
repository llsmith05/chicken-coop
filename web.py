from flask import Flask, render_template, url_for
from sensors import getTemp, c_to_f
app = Flask(__name__)

@app.route("/")
def coophome():
	temp = str(c_to_f(getTemp()))
	return render_template('main.html', temp=temp)

if __name__ == "__main__":
	app.run(host='0.0.0.0')
