from app import db, app
from flask import request
import twilio.twiml


@app.route("/", methods= ["GET", "POST"])
def replyToSms():
	messageBody = request.form.get('Body')
	resp = twilio.twiml.Response()
	resp.message("Hello, What is your Name?")
	return str(resp), 200, {"Content-Type":"application/xml; charset=utf-8"}