from web3 import Web3
import erc20



infura_url = "https://mainnet.infura.io/v3/7f9398e6cc404b89adf97d5e686efb5b"
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
print(web3.eth.blockNumber)

# "wallet" address hash
account = Web3.toChecksumAddress("0xaaca6c17b822a4b5074d4ca4dabd99a8bd04f41b")
balance = web3.eth.getBalance(account)
print("Ether balance: {0}".format(web3.fromWei(balance, "ether")))
print(web3.eth.get_transaction_count(account))

# opensea contract: 0x495f947276749ce646f68ac8c248420045cb7b5e
# contract = web3.eth.contract(abi=erc721_abi,
#                              address=Web3.toChecksumAddress("0x495f947276749ce646f68ac8c248420045cb7b5e"))
# print(contract.functions.symbol().call())
# print(contract.functions.abi)

# print(web3.eth.get_transaction("0xa3315a3ded75c66fe4461ec3043a9529ee844fafab01217bcadad884ac5ba41f"))

# polygon contract: 0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0
# token = web3.eth.contract(abi=erc20.erc20_human_standard_token_abi,
#                           address=Web3.toChecksumAddress("0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0"))
# print(
#     web3.fromWei(token.functions.balanceOf(Web3.toChecksumAddress("0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0")).call(),
#                  unit="ether"))
# print(token.functions.symbol().call())
# print(dir(token.functions))
# print(token.functions.abi)
# for f in token.functions:
#     print(f)

# husky token ID: 50830097462543580601473563981388698009005024090223633461481090199969251459172

