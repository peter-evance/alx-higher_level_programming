import urllib.request
import urllib.parse
import sys

# Get the URL and email from command-line arguments
url = sys.argv[1]
email = sys.argv[2]

# Prepare the data to be sent in the POST request
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

# Send the POST request and read the response
with urllib.request.urlopen(url, data) as response:
    body = response.read().decode('utf-8')

# Display the body of the response
print("Your email is:", email)
print("Response body:", body)
