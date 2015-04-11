# -*- coding: utf-8 -*
from app import db, app, models
from flask import request, jsonify, render_template
import twilio.twiml


@app.route("/", methods= ["GET", "POST"])
def home():
	if request.method == "POST":
		resp = twiml.Response()
		name = request.form.get('name')
		searchingForName = request.form.get('searchingForName')
		message = request.form.get('message')
		phoneNumber = request.form.get('phoneNumber')
	
		user = models.User(name, searchingForName, message, phoneNumber)
		db.session.add(user)
		db.session.commit()
		#search database and if there's a match, return relevant info.
		match = match(user.name, user.searchingForName) 
		if match != None:
			return jsonify({'name':match.name, 'searchingForName':match.searchingForName, "message":match.message})	
		else:
			return jsonify({"message: Bulletin posted. Pending match"})

	return render_template("index.html")



#This route is only called by Heroku
@app.route("/sms", methods= ["GET", "POST"])
def replyToSms():
	messageBody = request.form.get('Body')
	resp = twiml.Response()
	body = request.form.get('Body')
	tokens = re.sub(r'\s', '', body).split('*')
	# If the message is malformed, remind the user of format
	if (len(tokens) != 3):
		#resp.message("Sorry. Please use format: my name * their name * message")
		resp.message(u'عذراً. الرجاء إستعمال هذا التصميم : إسمي*اسمهم*الرسالة')
	else:
		#store into DB
		user = models.User(tokens[0], tokens[1], tokens[2])
		db.session.add(user)
		db.session.commit()
		#search database and if there's a match, return relevant info.
		match = match(user.name, user.searchingForName) 
		if match != None:
			res.message("Match Found. Match Name: "+match.name+". Message: "+match.message)
		# if no match, just say bulletin was posted but no match yet.	
		else:
			#resp.message("Bulletin posted. Pending match.")
			resp.message(u'لقد تم نشر هذا البيان | التطابق  في قيد الانتظار')
			
	return str(resp), 200, {"Content-Type":"application/xml; charset=utf-8"}





@app.route("/getUser")
def getUsers():
	users = models.User.query.all()
	user = users[0]
	return jsonify({'name':user.name, 'searchingForName':user.searchingForName, "message":user.message})
	#jsonify(results=users[0]),200, {"Content-Type":"application/json; charset=utf-8"}


#This function checks if there is a match between two people
def match(name, searchingFor):
	result = models.User.query.filter_by(name = searchingFor, searchingForName = name).first()
	if result == None:
		return None
	else:
		return str(result.name)
