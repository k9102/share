import re

dna = '''
>hg38_chr1:778686-778698(-)
CCGTGACGTCACA
>hg38_chr1:778710-778722(+)
TTGTGACGTCACA
>hg38_chr1:778711-778723(-)
CTGTGACGTCACA
>hg38_chr1:817310-817322(+)
TGTTCACGTCACC
'''

p = re.compile(r"chr(\d+):(\d+)-(\d+)\(([+-])\)")

r = p.findall(dna)
