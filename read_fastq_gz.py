#!/usr/bin/python3
"""code by ZhangW"""
import gzip
import os,sys

def read_fastq_gz(fp):#this code read *.fastq.gz file
        name, seq, qual = '', '', ''
        seq_bool, qual_bool =  False,False
        for line in fp: 
                l = line.decode()
                #print(l[:3], seq_bool, qual_bool)
                if l[0] == '@' and len(seq) <= len(qual): #fastq qual long enough
                        if seq != '' and len(seq) == len(qual):#good quality to produce
                                yield name, (seq, qual)
                        name = l[: -1]#remove \n, then start a new one
                        seq, qual = '', ''
                        seq_bool, qual_bool = True, False
                        continue
                if l[0] == '+' and not qual_bool:
                        seq_bool, qual_bool = False, True
                        continue
                if seq_bool and not qual_bool:
                        seq += l.strip()
                        continue
                if not seq_bool and qual_bool:
                        qual += l.strip()
                        continue
        yield name, (seq, qual)#yield the last read




fq = gzip.open(sys.argv[1])

for i,(name,(seq,qual)) in enumerate(read_fastq_gz(fq)):
	print(name, len(seq), len(qual))
