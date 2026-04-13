import gzip
import os
import ssl
import urllib.request

from Bio import SeqIO

def count_short_chains(filepath, length_cutoff):
    allrecords = 0
    count = 0

    with gzip.open(filepath, mode="rt") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            allrecords += 1
            # description の中から "length:xxx" を探して数値を取得
            for field in record.description.split():
                if field.startswith("length:"):
                    length = int(field.split(":")[1])
                    if length <= length_cutoff:
                        count += 1
                    break

    return allrecords, count  