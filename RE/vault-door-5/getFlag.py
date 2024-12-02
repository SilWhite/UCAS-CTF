import base64
import urllib.parse

# referece: ChatGPT


# The expected Base64 encoded string from the Java code
expected_base64 = (
    "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
    "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
    "JTM0JTVmJTY1JTMzJTMxJTM1JTMyJTYyJTY2JTM0"
)

# Step 1: Decode from Base64
decoded_base64 = base64.b64decode(expected_base64)

# Step 2: Decode from URL encoding
decoded_url = urllib.parse.unquote(decoded_base64.decode("utf-8"))

# Output the result
print("Decoded URL-encoded password:", decoded_url)
