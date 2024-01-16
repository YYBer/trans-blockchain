import os
print(f"I am here: {os.getcwd()}")
from web3 import Web3
import json
# from views import result

with open('./blockchainTestApp/trans.abi', 'r') as abi_file:
    abi = json.load(abi_file)
with open('./blockchainTestApp/trans.bin', 'r') as bin_file:
    bytecode = bin_file.read()

provider_rpc = {
    "development": "http://localhost:9944",
    "sepolia": "https://eth-sepolia.g.alchemy.com/v2/9X0WvOag2Ac3dAO8p9rOiU6G95Xkg5zb",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["sepolia"]))

account_from = {
    'private_key': '4ae1cc01b339a6e3691f3df17392a1b49b25111ea4a828fc54edad7d29c111b2',
    'address': '0xD20D8879EdC62684Ba82ebE37e97984Dd5Aae287',
}
address_to = '0x0C7f3ff8EFEB99053BEa51b041ec954BA26c4FD6'
trans = web3.eth.contract(abi=abi, bytecode=bytecode)
current_nonce = web3.eth.get_transaction_count(account_from["address"])
nonce = current_nonce + 7
result = "11111,aa01,bb12" 
binary_result = result.encode('utf-8')
construct_txn = trans.functions.save(binary_result).build_transaction(
    {
        "from": Web3.to_checksum_address(account_from["address"]),
        # "nonce": web3.eth.get_transaction_count(Web3.to_checksum_address(account_from["address"])),
        "gas": 10000000,
        "gasPrice": web3.to_wei('50','gwei'),
        "to": Web3.to_checksum_address(address_to),
        "nonce": nonce,
    }
)

tx_create = web3.eth.account.sign_transaction(
    construct_txn, account_from["private_key"]
)

tx_hash = web3.eth.send_raw_transaction(tx_create.rawTransaction)
# tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=300)
print(f'Contact transaction hash {tx_hash.hex()}')
# print(f"Contract deployed at address {tx_receipt.contractAddress}")

# This approach skips waiting for the transaction receipt, which includes additional information such as the status, cumulative gas used, and logs. If you only need the transaction hash and don't require additional details, this method is more efficient.
