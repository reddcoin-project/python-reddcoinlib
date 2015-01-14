#!/usr/bin/env python
#
# Copyright (C) 2013-2014 The python-bitcoinlib developers
# Copyright (C) 2014-2015 The python-reddcoinlib developers
#
# This file is part of python-reddcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

"""Make a bootstrap.dat file by getting the blocks from the RPC interface."""

import struct
import sys
import time

import reddcoin
import reddcoin.rpc
from reddcoin.core import CBlock


try:
    if len(sys.argv) not in (2, 3):
        raise Exception

    n = int(sys.argv[1])

    if len(sys.argv) == 3:
        reddcoin.SelectParams(sys.argv[2])
except Exception as ex:
    print('Usage: %s <block-height> [network=(mainnet|testnet|regtest)] > bootstrap.dat' % sys.argv[0])
    sys.exit(1)


proxy = reddcoin.rpc.Proxy()
total_bytes = 0
start_time = time.time()
fd = sys.stdout

for i in range(n + 1):
    block = proxy.getblock(proxy.getblockhash(i))
    block_bytes = block.serialize()
    total_bytes += len(block_bytes)

    print('%.2f KB/s, height %d, %d bytes' % ((total_bytes / 1000) / (time.time() - start_time), i, len(block_bytes)))

    fd.write(reddcoin.params.MESSAGE_START)
    fd.write(struct.pack('<i', len(block_bytes)))
    fd.write(block_bytes)
