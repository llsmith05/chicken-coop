import sqlite3 as lite
import sys


con = lite.connect('coop.db')

with con:
	cur = con.cursor()
	#cur.execute('SELECT max(id) FROM coop_data')
	#lid = cur.fetchone()[0]
	d1 = 5
	d2 = 80
	d3 = 0
	cur.execute('INSERT INTO coop_data (count, temp, door) VALUES (?, ?, ?)', (d1, d2, d3))
	
	cur.execute('SELECT * FROM coop_data WHERE id=(SELECT max(id) FROM coop_data)')
	row = cur.fetchone()

	chickenCount = row[1]
	temp = row[2]
	doorStatus = row[3]
	print "count: " + str(chickenCount) + "temp: " + str(temp) + "door: " + str(doorStatus)

