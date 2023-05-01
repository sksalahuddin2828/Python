from twilio.rest import Client

# Replace with your Twilio account SID and auth token
account_sid = 'twilio_account_SID'
auth_token = 'twilio_auth_token'

# Replace with your Twilio phone number and target phone number
twilio_number = 'twilio_number_generate_it_from_twilio'
target_number = '(+64) adding+country_code + where_you_send_message_his/her_mobile/cellPhone_number'

# Create the Twilio client
client = Client(account_sid, auth_token)

# Send a message
message = client.messages.create(
    body="খবর আছে তোর! খাইছি তোরে", # "This is a random message or Testing message"
    from_=twilio_number,
    to=target_number
)

# Print the message body
print(message.body)
