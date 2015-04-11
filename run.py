from flask import Flask
from flask import request
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods= ["GET", "POST"])
def replyToSms():
	print request.data
	resp = twilio.twiml.Response()
	resp.message("What is your Name?")
	return str(resp), 200, {"Content-Type":"application/xml; charset=utf-8"}

if __name__ == "__main__":
    app.run(debug=True)
