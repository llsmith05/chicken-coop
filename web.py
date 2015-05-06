from flask import Flask, render_template, url_for
import sqlite3 as lite
import sys
#from myrpio import getchickenCount
app = Flask(__name__)

#con = None

#doorStatus
#chickenCount
#temp = 65

@app.route("/")
def coophome():
	con = lite.connect('coop.db')

	with con:
		cur = con.cursor()
		cur.execute("SELECT * FROM coop_data WHERE id=(SELECT max(id) FROM coop_data)")
		row = cur.fetchone()
		
		chickenCount = row[1]
		temp = row[2]
		doorStatus = row[3]
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
	app.run(host='0.0.0.0')
