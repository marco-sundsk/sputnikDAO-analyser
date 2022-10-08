#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Marco'

try:
    from rpc_info import TESTNET_RPC_URL, MAINNET_RPC_URL
except ImportError:
    TESTNET_RPC_URL= ["https://rpc.testnet.near.org", ]
    MAINNET_RPC_URL= ["https://rpc.mainnet.near.org", ]


"""

"""

class Cfg:
    NETWORK_ID = "MAINNET"
    NETWORK = {
        "TESTNET": {
            "NEAR_RPC_URL": TESTNET_RPC_URL,
            "DAO_CONTRACT": "ref-finance.sputnik-dao.testnet",
        },
        "MAINNET": {
            "NEAR_RPC_URL": MAINNET_RPC_URL,
            "DAO_CONTRACT": "ref-finance.sputnik-dao.near",
        }
    }


if __name__ == '__main__':
    print(type(Cfg))
    print(type(Cfg.NETWORK_ID), Cfg.NETWORK_ID)
    print(Cfg.NETWORK["TESTNET"]["NEAR_RPC_URL"])