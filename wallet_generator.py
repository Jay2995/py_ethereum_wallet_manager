import os
from eth_keys import keys

def generate_ethereum_wallet():
    private_key_bytes = os.urandom(32)
    private_key = keys.PrivateKey(private_key_bytes)

    address = private_key.public_key.to_checksum_address()
    wallet_info = {
        "private_key": private_key,
        "address": address

    }

    return wallet_info;

