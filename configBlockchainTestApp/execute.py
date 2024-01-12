import os
solcx.install_solc("0.8.23")
from deploy_sepo import tx_hash

print("abc!")
# os.system("python3 deploy_sepo.py")
# print("okay!")
test = tx_hash
print(f"test: {test.hex()}")