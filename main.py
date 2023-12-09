


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from eth_keys import keys

def generate_ethereum_wallet():
    # Generate a new private key
    private_key = keys.PrivateKey.create()

    # Get the corresponding Ethereum address
    address = private_key.public_key.to_checksum_address()

    return private_key, address

if __name__ == "__main__":
    # Generate a new Ethereum wallet
    private_key, address = generate_ethereum_wallet()

    # Print the private key and address (for demonstration purposes)
    print("Private Key:", private_key)
    print("Address:", address)