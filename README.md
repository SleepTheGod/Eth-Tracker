Explanation
fetch_transactions: This function fetches all transactions for a given Ethereum address using the Etherscan API.
wei_to_ether: This function converts the value from Wei (the smallest denomination of Ether) to Ether.
process_transactions: This function processes the transaction data, displaying the transactions and recursively tracking subsequent transactions up to the specified depth.
track_wallet_transactions: This is the main function that starts tracking transactions for a given Ethereum address and specified depth.

Usage
Obtain an API key from Etherscan by signing up for a free account.
Run the script and enter the Ethereum wallet address, your Etherscan API key, and the depth of transaction tracking when prompted.
The script will print the transaction history and recursively track transactions for addresses that receive funds from the specified wallet up to the specified depth.
