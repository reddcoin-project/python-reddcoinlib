# Copyright (C) 2012-2014 The python-bitcoinlib developers
#
# This file is part of python-bitcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

from __future__ import absolute_import, division, print_function, unicode_literals

import reddcoin.core


class MainParams(reddcoin.core.CoreChainParams):
    MESSAGE_START = b'\xfb\xc0\xb6\xdb'
    DEFAULT_PORT = 45444
    RPC_PORT = 45443
    DNS_SEEDS = (('reddcoin.com', 'seed.reddcoin.com'))
    BASE58_PREFIXES = {'PUBKEY_ADDR': 61,
                       'SCRIPT_ADDR': 5,
                       'SECRET_KEY': 189}


class TestNetParams(reddcoin.core.CoreTestNetParams):
    MESSAGE_START = b'\x0b\x11\x09\x07'
    DEFAULT_PORT = 18333
    RPC_PORT = 18332
    DNS_SEEDS = (('bitcoin.petertodd.org', 'testnet-seed.bitcoin.petertodd.org'),
                 ('bluematt.me', 'testnet-seed.bluematt.me'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}

class RegTestParams(reddcoin.core.CoreRegTestParams):
    MESSAGE_START = b'\xfa\xbf\xb5\xda'
    DEFAULT_PORT = 18444
    RPC_PORT = 18332
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}

"""Master global setting for what chain params we're using.

However, don't set this directly, use SelectParams() instead so as to set the
reddcoin.core.params correctly too.
"""
#params = reddcoin.core.coreparams = MainParams()
params = MainParams()

def SelectParams(name):
    """Select the chain parameters to use

    name is one of 'mainnet', 'testnet', or 'regtest'

    Default chain is 'mainnet'
    """
    global params
    reddcoin.core._SelectCoreParams(name)
    if name == 'mainnet':
        params = reddcoin.core.coreparams = MainParams()
    elif name == 'testnet':
        params = reddcoin.core.coreparams = TestNetParams()
    elif name == 'regtest':
        params = reddcoin.core.coreparams = RegTestParams()
    else:
        raise ValueError('Unknown chain %r' % name)
