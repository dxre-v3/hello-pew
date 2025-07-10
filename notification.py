
# Imports:
import json
import requests
import sys


# Set the headers for the post to Slack
headers = {
	'Content-type': 'application/json',
}

# Get the message to send
status = sys.argv[1]
message = ":partying_face: `Hello-World` has deployed." if ( status == "true" ) else ":looking: `Hello-World` failed to deploy.";

# Fill in the content using the Slack Block 
set_blocks = {
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": message
			}
		}
	]
}

# Prep for sending 
blocks = json.dumps(set_blocks)

# Post to Slack
requests.post( sys.argv[2], headers=headers, data=blocks.encode('utf-8'))



