from twilio.rest import TwilioRestClient
import settings
client = TwilioRestClient(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
message = client.messages.create(to="+971501067468", from_=settings.FROM_NUMBER, body="Testing Twilio")


