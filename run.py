# -*- coding: utf-8 -*-

import re
from flask import Flask
from flask import request
from twilio import twiml
from app import app

app = Flask(__name__)

@app.route("/", methods= ["GET", "POST"])
def replyToSms():
	resp = twiml.Response()
	body = request.form.get('Body')
	tokens = re.sub(r'\s', '', body).split('*')
	# If the message is malformed, remind the user of format
	if (len(tokens) != 3):
		#resp.message("Sorry. Please use format: my name * their name * message")
		resp.message(u'عذراً. الرجاء إستعمال هذا التصميم : إسمي*اسمهم*الرسالة')
	else:
		# TODO : store into DB
		# TODO : search database and if there's a match, return relevant info. 
		#resp.message("Bulletin posted. Pending match.")
		resp.message(u'لقد تم نشر هذا البيان | التطابق  في قيد الانتظار')
		# if no match, just say bulletin was posted but no match yet.
	return str(resp)

if __name__ == "__main__":
    app.run(debug=True)