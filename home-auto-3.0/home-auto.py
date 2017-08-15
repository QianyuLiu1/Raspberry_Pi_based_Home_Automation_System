from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, session
from flask import jsonify
from business import controlLed, getVideo_IP, startVideo, getSensor_Data

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
def loing_form():
	return render_template('login.html')

#form must specify the methods parameters,otherwise bug
@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		name = request.form['username']
		pwd = request.form['password']
		print(name)
		print(pwd)
		return redirect(url_for('reMain'))

@app.route('/reMain')
def reMain():
	return render_template('main.html')

@app.route('/control', methods=['GET','POST'])
def controlled():
	if request.method == 'POST':
		value = request.form['value']
		device = request.form['device']
		msg = device + ':' + value
		print(msg)
		controlLed(device,value)
		return jsonify({'data':'50'})

@app.route('/getSensorData', methods=['GET','POST'])
def getSensorData():
	if request.method == 'POST':
		value = request.form['value']
		device = request.form['device']
		msg = device + ':' + value
		print(msg)

		data = 2020
		if 'sensor' in session:
			data = session['sensor']
		else:
			data = getSensor_Data(device)
			session['sensor'] = data
		humidity = data/100
		temperature = data%100
		return jsonify({'humidity':humidity, 'temperature':temperature})

@app.route('/getVideoIP', methods=['GET','POST'])
def getVideoIP():
	if request.method == 'POST':
		value = request.form['value']
		device = request.form['device']
		msg = device + ':' + value
		print(msg)
		ip = getVideo_IP()
		startVideo()
		return jsonify({'ip':ip})
		

if __name__=='__main__':
	app.run(host='0.0.0.0', port=80)
