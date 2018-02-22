#!/usr/bin/env python3
# author wf
# -*- coding: utf-8 -*-

from coinmarketcap import Market
import sys
import argparse


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument('currency', help="curency")
    parser.add_argument('key', help="Выводимый ключ")
    parser.add_argument('convert', help="convert to", default='USD')
    args = parser.parse_args(arguments)
    print(args.currency)
    coinmarketcap = Market()
    print(coinmarketcap.ticker(args.currency, limit = 1, convert = args.currency))
    print(coinmarketcap.ticker(args.currency, limit = 1, convert = args.currency)[0].get(args.key))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))