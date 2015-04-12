# -*- coding: utf-8 -*
from app import db, app, models
from flask import request, jsonify, render_template, g
import twilio.twiml
import re
from twilio.rest import TwilioRestClient
import settings

@app.before_request
def before_request():
	g.client = TwilioRestClient(settings.ACCOUNT_SID, settings.AUTH_TOKEN)


@app.route("/", methods= ["GET", "POST"])
def home():
	if request.method == "POST":
		name = request.form.get('name')
		searchingForName = request.form.get('searchingForName')
		message = request.form.get('message')
		phoneNumber = request.form.get('phoneNumber')
		
		user = models.User(name, searchingForName, message, phoneNumber)
		db.session.add(user)
		db.session.commit()
		#search database and if there's a match, return relevant info.
		matchFound = match(user.name, user.searchingForName) 
		if matchFound:
			g.client.messages.create(to=matchFound.phoneNumber, from_=settings.FROM_NUMBER, body=message)
			g.client.messages.create(to=phoneNumber, from_=settings.FROM_NUMBER, body=matchFound.message)
			return jsonify({'name':matchFound.name, 'searchingForName':matchFound.searchingForName,\
			 "message":matchFound.message, "phone":matchFound.phoneNumber})	
		else:
			return jsonify({})

	return render_template("home.html")
	#render_template("home.html")



#This route is only called by Twilio
@app.route("/sms", methods= ["GET", "POST"])
def replyToSms():
	messageBody = request.form.get('Body')
	resp = twilio.twiml.Response()
	senderPhone = request.form.get('From')
	body = request.form.get('Body')
	#body = body[::-1]
	tokens = [item.strip() for item in body.split('*')]
	print tokens
	# If the message is malformed, remind the user of format
	if (len(tokens) != 3):
		#resp.message("Sorry. Please use format: my name * their name * message")
		resp.message(u'عذراً. الرجاء إستعمال هذا التصميم : إسمي*اسمهم*الرسالة')

	else:
		#store into DB
		user = models.User(tokens[0], tokens[1], tokens[2], senderPhone)
		db.session.add(user)
		db.session.commit()
		#search database and if there's a match, return relevant info.
		matchFound = match(user.name, user.searchingForName) 
		print matchFound
		if matchFound:
			print"MATCH FOund"
			g.client.messages.create(to=matchFound.phoneNumber,\
			 from_=settings.FROM_NUMBER, body=u'وجدناهم! الاسم:'+matchFound.name+u'. الهاتف:'+matchFound.phoneNumber+u'. الرسالة: '+tokens[2])
			resp.message(u'وجدناهم! الاسم:'+matchFound.name+u'. الهاتف:'+matchFound.phoneNumber+u'. الرسالة: '+matchFound.message)
			

		# if no match, just say bulletin was posted but no match yet.	
		else:
			#resp.message("Bulletin posted. Pending match.")
			resp.message(u'لقد تم نشر هذا البيان | التطابق  في قيد الانتظار. عبر تسليم هذه الرسالة أنت توافق على تبادل هذه المعلومات')
			
	return str(resp), 200, {"Content-Type":"application/xml; charset=utf-8"}





@app.route("/getUser")
def getUsers():
	return request.form.get('name')
	users = models.User.query.all()
	user = models.User.query.filter_by(name = request.form.get('name')).first()
	return jsonify({'name':user.name, 'searchingForName':user.searchingForName, "message":user.message})
	#jsonify(results=users[0]),200, {"Content-Type":"application/json; charset=utf-8"}


#This function checks if there is a match between two people
def match(name, searchingFor):
	print name
	print searchingFor
	result = models.User.query.filter_by(name = searchingFor, searchingForName = name).first()
	print result
	return result
