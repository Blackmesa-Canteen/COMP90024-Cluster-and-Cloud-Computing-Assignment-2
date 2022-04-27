# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     id_file_zipper
   Description :

   Helper script to zip id files to save disk space.
   Put this script in the `COVID-19-TweetIDs` open-source project's folder,
    and run it to compress all ID txt files.

   Author :       Xiaotian Li
   date：          27/04/2022
-------------------------------------------------
"""
import gzip
import os.path
import random

from pathlib import Path

# data_dirs = ['2020-01', '2020-02', '2020-03',
# '2020-04', '2020-05', '2020-06', '2020-07',
# '2020-08', '2020-09', '2020-10', '2020-11', '2020-12']
data_dirs = ['2020-07', '2020-08', '2020-09']


def main():
    for data_dir in data_dirs:
        for path in Path(data_dir).iterdir():
            if path.name.endswith('txt'):
                partial_zipping(path)


def _reader_generator(reader):
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024 * 1024)


def raw_newline_count(fname):
    """
    Counts number of lines in file
    """
    f = open(fname, 'rb')
    f_gen = _reader_generator(f.raw.read)
    return sum(buf.count(b'\n') for buf in f_gen)


def total_zipping(id_file):
    """
    zip all ID files
    """
    gzip_path = id_file.with_suffix('.gz')

    f_out = gzip.open(os.path.join('compressed', gzip_path), mode='wb')
    f_in = open(id_file, "rb")

    f_out.writelines(f_in)
    f_out.close()
    f_in.close()


def partial_zipping(id_file):
    """
    zip partial IDs, that are randomly simpled
    """
    gzip_path = id_file.with_suffix('.gz')

    # you need manually provide empty folders such as 2020-07 in the ./compressed folder
    f_out = gzip.open(os.path.join('compressed', gzip_path), mode='wb')

    # random sample rows 1/300
    total_raws = raw_newline_count(id_file)
    num_samples = int(total_raws * (1 / 300))

    if num_samples > 0:
        resultList = random.sample(range(0, total_raws), num_samples)

        f_in = open(id_file, "rb")
        lines = f_in.readlines()

        for i in resultList:
            f_out.write(lines[i])

        f_out.close()
        f_in.close()


if __name__ == "__main__":
    main()