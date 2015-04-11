from app import db, app, models
from flask import request, jsonify
import twilio.twiml



@app.route("/", methods= ["GET", "POST"])
def replyToSms():
	messageBody = request.form.get('Body')



	user = models.User("Joe Jean", "Obama", "Hello Mr President", "12345566")
	db.session.add(user)
	db.session.commit()
	resp = twilio.twiml.Response()
	resp.message("Hello, What is your Name?")
	return str(resp), 200, {"Content-Type":"application/xml; charset=utf-8"}

@app.route("/getUser")
def getUsers():
	users = models.User.query.all()
	user = users[0]
	return jsonify({'firstName':user.firstName, 'searchingForName':user.searchingForName, "message":user.message})
	#jsonify(results=users[0]),200, {"Content-Type":"application/json; charset=utf-8"}

