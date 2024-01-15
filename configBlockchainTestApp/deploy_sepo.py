# import os
# from compile_sepo import abi, bytecode
from web3 import Web3
import json
# from views import result

with open('.trans.abi', 'r') as abi_file:
    abi = json.load(abi_file)
with open('.trans.bin', 'r') as bin_file:
    bytecode = bin_file.read()

provider_rpc = {
    "development": "http://localhost:9944",
     "sepolia": "https://endpoints.omniatech.io/v1/eth/sepolia/public",
}

web3 = Web3(Web3.HTTPProvider(provider_rpc["sepolia"]))

account_from = {
    'private_key': '4ae1cc01b339a6e3691f3df17392a1b49b25111ea4a828fc54edad7d29c111b2',
    'address': '0xD20D8879EdC62684Ba82ebE37e97984Dd5Aae287',
}
address_to = '0x0C7f3ff8EFEB99053BEa51b041ec954BA26c4FD6'
trans = web3.eth.contract(abi=abi, bytecode=bytecode)
#GameID player1_name player1_points player2_name player2_points
result = "12443,zz03,yy12" 
binary_result = result.encode('utf-8')
construct_txn = trans.functions.save(binary_result).build_transaction(
    {
        "from": Web3.to_checksum_address(account_from["address"]),
        "nonce": web3.eth.get_transaction_count(Web3.to_checksum_address(account_from["address"])),
        "gas": 10000000,
        "gasPrice": web3.to_wei('60','gwei'),
        "to": Web3.to_checksum_address(address_to),
    }
)

tx_create = web3.eth.account.sign_transaction(
    construct_txn, account_from["private_key"]
)

tx_hash = web3.eth.send_raw_transaction(tx_create.rawTransaction)
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=300)

print(f'Contact transaction hash {tx_hash.hex()}')
# print(f"Contract deployed at address {tx_receipt.contractAddress}")
