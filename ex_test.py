import unittest
from encryption import generate_hmac, verify_hmac  # Import your functions

class TestHmacFunctions(unittest.TestCase):

    def setUp(self):
        """Setup test variables"""
        self.key = b"test_key"
        self.message = "Hello, world!"
        self.hmac_value = generate_hmac(self.key, self.message)

    def test_generate_hmac(self):
        """Test HMAC generation"""
        self.assertIsInstance(self.hmac_value, str)
        self.assertEqual(len(self.hmac_value), 64)  # SHA-256 produces 64-character hex

    def test_verify_hmac_valid(self):
        """Test HMAC verification with correct values"""
        self.assertTrue(verify_hmac(self.key, self.message, self.hmac_value))

    def test_verify_hmac_invalid(self):
        """Test HMAC verification with incorrect values"""
        fake_hmac = "neeti123" * 10
        self.assertFalse(verify_hmac(self.key, self.message, fake_hmac))

if __name__ == '__main__':
    unittest.main()
