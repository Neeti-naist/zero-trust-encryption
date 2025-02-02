import hmac
import hashlib
def generate_hmac(key, message):
    """
    Generate hmac for the message using the provided key
    :param key: Secret key for hmac gen
    :param message: message to be hashed
    :return: Hmac hex digest
    """
    #create a new hmac object using the key and sha-256 as the hash function#

    hmac_object = hmac.new(key.encode(), message.encode(), hashlib.sha256 )
    return hmac_object.hexdigest()  # return hmac as a hexadecimal string

def verify_hmac(key, message, received_hmac):
    """
    verify the integrity of the message by comparing the generated hmac with the received hmac
    :param key: secret key for hmac gen
    :param message:Original message
    :param received_hmac: hmac received with the message
    :return:Boolean indicating whether the hmac is valid
    """
    #generate hmac for og message
    generated_hmac = generate_hmac(key, message)
    return hmac.compare_digest(generated_hmac, received_hmac) #compare the generated hmac with the received hmac


#example _usage
if __name__ == "__main__":
    secret_key ="my_secret_key"
    original_message = "This is a secret message"

    #generate hmac
    hmac_value = generate_hmac(secret_key,original_message)
    print("Generated hmac: ", hmac_value)
    #verify hmac
    is_valid = verify_hmac(secret_key, original_message, hmac_value)
    print("Is hmac valid? ", is_valid)





