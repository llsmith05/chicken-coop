from flask import Flask
from sensors import getTemp
app = Flask(__name__)

@app.route("/")
def hello():
	return "Temp is " + str(getTemp())

if __name__ == "__main__":
	app.run(debug=True)
