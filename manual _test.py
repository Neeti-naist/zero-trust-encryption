from encryption import generate_hmac, verify_hmac
if __name__ == "__main__":
    secret_key = b"my_secret_key"  # Key in bytes
    original_message = "This is a secret message"

    # Generate HMAC
    hmac_value = generate_hmac(secret_key, original_message)
    print("Generated HMAC:", hmac_value)

    # Verify HMAC
    is_valid = verify_hmac(secret_key, original_message, hmac_value)
    print("Is HMAC valid?", is_valid)

    # Testing with a tampered message
    altered_message = "This is a hacked message"
    is_altered_valid = verify_hmac(secret_key, altered_message, hmac_value)
    print("Is tampered message valid?", is_altered_valid)  # Should print False
