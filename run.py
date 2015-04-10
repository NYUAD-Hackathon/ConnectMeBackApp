from flask import Flask
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods= ["GET", "POST"])
def replyToSms():
	resp = twilio.twiml.Response()
	resp.message = ("What is your Name?")
	return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
