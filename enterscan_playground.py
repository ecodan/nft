import datetime
import time

from etherscan import Etherscan
from web3 import Web3

# infura_url = "https://mainnet.infura.io/v3/7f9398e6cc404b89adf97d5e686efb5b"
# web3 = Web3(Web3.HTTPProvider(infura_url))
# print(web3.isConnected())
wei_to_ether = 1 * 10**18

account = "0xaaca6c17b822a4b5074d4ca4dabd99a8bd04f41b"
opensea_contract = "0x495f947276749ce646f68ac8c248420045cb7b5e"
api_key = "XRMT19VAS4QYXICT8EEZX6JHHHBWEKN9NQ"
eth = Etherscan(api_key)
print(int(eth.get_eth_balance(address=account))/wei_to_ether)
ts = time.time()
block = eth.get_block_number_by_timestamp(timestamp=int(ts), closest="before")

#print(eth.get_normal_txs_by_address(address=account, startblock=1, endblock=block, sort="desc" ))

print(eth.get_erc721_token_transfer_events_by_address_and_contract_paginated(
    address=account,
    contract_address=opensea_contract,
    sort="desc",
    page=1,
    offset=1,
))