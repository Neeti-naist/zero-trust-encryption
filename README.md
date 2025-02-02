# zero-trust-encryption
Python encryption for Zero-Trust-Project
Explanation of the code:
1. Generate_hmac function:
Purpose: generates a Mac for a given message using a secret key.
Parameters: 
Key: a secret key known only to the sender and receiver.
Message: the data for which integrity needs to be ensured .
process:
The hmac.new()function creates an hmac object using the key and the message.
The hash lib.sha256 specifies the hash function to be used (SHA-256) in this case.
The hexdigest() method returns the HMAC as a hexadecimal string.
2. Verify_hmac function:
Purpose: verifies the integrity of the message by comparing the generated hmac with the received hmac.
Parameters: 
Key: the same secret key used to generate the hmac
Message: the original message
received_hmac: the hmac received with the message.
Process:
The function generates the hmac for the original message.
It then compares the generated hmac with the received hmac using hmac.compare_digest(), which is a secure way to compare hashes.

Example usage:
A secret key and a message are defined.
The hmac is generated and printed
The hmac is then verified , and the result is printed.
