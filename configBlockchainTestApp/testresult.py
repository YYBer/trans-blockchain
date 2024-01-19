from web3 import Web3

# Assuming 'web3' is your Web3 instance
tx_hash = "0xYourTransactionHash"

try:
    tx_receipt = web3.eth.getTransactionReceipt(tx_hash)
    if tx_receipt is not None:
        print(f"Transaction {tx_hash} already mined.")
    else:
        print(f"Transaction {tx_hash} is still pending.")
except Exception as e:
    print(f"Error checking transaction status: {e}")

