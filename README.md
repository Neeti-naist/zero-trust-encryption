# zero-trust-encryption
Python encryption for Zero-Trust-Project(HMAC implementation)
Explanation of the code:-------------------------------------------------------
**1. generate_hmac (key, message):**
Purpose: generates a hMac for a given message using a secret key.
Parameters: 
Key: a secret key known only to the sender and receiver.
Message: the data for which integrity needs to be ensured .
process:
The hmac.new()function creates an hmac object using the key and the message.
The hash lib.sha256 specifies the hash function to be used (SHA-256) in this case.
The hexdigest() method returns the HMAC as a hexadecimal string.---------------
**2. Verify_hmac (key, message, received_hmac):**
Purpose: verifies the integrity of the message by comparing the generated hmac with the received hmac.
Parameters: 
Key: the same secret key used to generate the hmac
Message: the original message
received_hmac: the hmac received with the message.
Process:
The function generates the hmac for the original message.
It then compares the generated hmac with the received hmac using hmac.compare_digest(), which is a secure way to compare hashes.----------------

**Example usage:**
A secret key and a message are defined.
The hmac is generated and printed
The hmac is then verified , and the result is printed.-------------------------

**Summary:**
Efficiency: Avoid redundant encoding, reducing CPU cycles.
Security Improvement: Uses hmac.compare_digest() to prevent timing attacks.
Testing support: Added a structured unittest setup for automated testing.
