wdir = 'C:/Users/batagelj/Documents/manuscripts/ESNAM2'
# tdir = 'C:/Users/batagelj/Documents/manuscripts/ESNAM2/Pajek/'
# tdir = 'C:/Users/batagelj/Documents/manuscripts/ESNAM2/sources/'
tdir = 'C:/Users/batagelj/Documents/manuscripts/ESNAM2/semirings/'
fname = 'manuscript.html'; cname = 'corrected.html'

import sys, os
sys.path = [wdir]+sys.path
os.chdir(wdir)

ls = r"\({\rm{\mathord{\buildrel{\lower3pt\hbox{$\scriptscriptstyle\smile$}}\over "
rs = r"} }}\)"
ch = ls+'c'+rs; sh = ls+'s'+rs; zh = ls+'z'+rs
ci = "\n     <cite>"
lsub = "</span> \n          <sub> <span"; rsub = "</span> </sub>"
txt = open(tdir+fname,"r",encoding="utf-8").read()

k = 0; again = True; ter = ''
while again:
  i = txt.find(ls,k)
  if i > 0:
    j = txt.find('\n',i-50)
    cha = txt[i+75]
    if cha=="c": uch = "č"
    elif cha == "s": uch = "š"
    elif cha == "z": uch = "ž"
    else: uch = "***"
    ter = ter + txt[k:j]+uch
    k = i+89
  else:    
    again = False
    ter = ter + txt[k:]

ter = ter.replace(ci,"<cite>").\
      replace(lsub,"</span><sub><span").replace(rsub,"</span></sub>")

out = open(tdir+cname,"w",encoding="utf-8")
out.write(ter); out.close()

    
