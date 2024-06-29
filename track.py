import requests
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from datetime import datetime

# Function to fetch transactions for a given Ethereum address
def fetch_transactions(address, api_key):
    url = 'https://api.etherscan.io/api'
    params = {
        'module': 'account',
        'action': 'txlist',
        'address': address,
        'startblock': 0,
        'endblock': 99999999,
        'sort': 'asc',
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['result']

# Function to convert Wei to Ether
def wei_to_ether(wei):
    return int(wei) / 10**18

# Function to process transactions and track subsequent transactions
def process_transactions(address, transactions, api_key, depth=2, current_depth=0):
    df = pd.DataFrame(transactions)
    df['timeStamp'] = pd.to_datetime(df['timeStamp'], unit='s')
    df['value'] = df['value'].apply(wei_to_ether)
    
    # Display the transaction history
    print(f"Transactions for {address}:")
    print(df[['timeStamp', 'from', 'to', 'value', 'hash']])
    
    # Recursively track subsequent transactions
    if current_depth < depth:
        for to_address in df['to'].unique():
            if to_address != address:
                next_transactions = fetch_transactions(to_address, api_key)
                process_transactions(to_address, next_transactions, api_key, depth, current_depth + 1)

# Main function to track transactions for a given address
def track_wallet_transactions(address, api_key, depth=2):
    transactions = fetch_transactions(address, api_key)
    process_transactions(address, transactions, api_key, depth)

# Run the tracker
if __name__ == "__main__":
    address = input("Enter the Ethereum wallet address: ")
    api_key = input("Enter your Etherscan API key: ")
    depth = int(input("Enter the depth of transaction tracking: "))
    track_wallet_transactions(address, api_key, depth)
