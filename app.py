import base64


def encode_string(original_str):
    # Encode the original string to Base64
    encoded_str = base64.b64encode(original_str.encode()).decode()

    # Take the first 20 characters of the encoded string
    reduced_str = encoded_str[:20]
    return reduced_str


def decode_string(reduced_str):
    # Decode the reduced string from Base64
    decoded_str = base64.b64decode(reduced_str.encode()).decode()
    return decoded_str


# Example usage:
original_string = "ABCDABCDABCDABCDABCDABCDABCDABCDABCDABCD"
encoded_string = encode_string(original_string)
decoded_string = decode_string(encoded_string)

print("Original String:", original_string)
print("Encoded and Reduced String:", encoded_string)
print("Decoded String:", decoded_string)