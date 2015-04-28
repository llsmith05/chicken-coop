from flask import Flask, render_template, url_for
app = Flask(__name__)

doorStatus = 0

@app.route("/")
def coophome():
	temp = 65
	chickenCount = 3
	return render_template('main.html', temp=temp, chickenCount=chickenCount, doorStatus=doorStatus)

@app.route("/door")
def doorToggle():
	global doorStatus
	if (doorStatus == 0):
		doorStatus = 1
		return "Opened!"
	else:
		doorStatus = 0
		return "Closed!"

if __name__ == "__main__":
	app.run(debug=True)
