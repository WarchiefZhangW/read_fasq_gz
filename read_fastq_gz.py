#!/usr/bin/python3
"""code by ZhangW"""
import gzip
import os,sys

def read_fastq_gz(fp):#this code read *.fastq.gz file
	name, seq, qual = '', '', ''
	for line in fp: 
		l = line.decode()
		if l[0] in '>@': 
			if seq != '':
				yield name, (seq, qual)
			name = l[: -1]#remove \n
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
