import os
# solcx.install_solc("0.8.23")
from deploy_sepo import tx_hash

print("abc!")
# os.system("python3 deploy_sepo.py")
# print("okay!")
test = tx_hash
print(f"test: {test.hex()}")

# import os
# import json

# # Get the absolute path of the current script
# script_dir = os.path.dirname(os.path.abspath(__file__))

# # Construct paths to ABI and BIN files in the same folder
# abi_file_path = os.path.join(script_dir, 'trans.abi')
# bin_file_path = os.path.join(script_dir, 'trans.bin')

# # Read ABI from file
# with open(abi_file_path, 'r') as abi_file:
#     abi = json.load(abi_file)

# # Read BIN from file
# with open(bin_file_path, 'r') as bin_file:
#     bin_code = bin_file.read()

# # Now you have 'abi' (as a Python list) and 'bin_code' (as a string)
