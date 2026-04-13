#!/usr/bin/env python3
from argparse import ArgumentParser

from kadaie1.core import count_short_chains


def main():
    parser = ArgumentParser(description="Count short chains in pdb_seqres.txt.gz")
    parser.add_argument("-i", "--input", type=str, required=True, help="Path to pdb_seqres.txt.gz")
    parser.add_argument("-l", "--length", type=int, required=True, help="Length cutoff")
    args = parser.parse_args()

    allrecords, count = count_short_chains(args.input, args.length)
    print(f"全レコード数: {allrecords}")
    print(f"残基長{args.length}以下のレコード数: {count}")
    print(f"存在比率: {count / allrecords * 100:.2f}%")


if __name__ == "__main__":
    main()