#!/usr/bin/python
# -*- coding: UTF-8 -*-

import linecache

def dupfile(srcfilename, dstfilename, count):
  lines = linecache.getlines(srcfilename)

  filterTotal = filter(lambda line:(len(line) >= 4) and (line[0:4]!="TLRL"), lines*count)
  finalLines = filterTotal + ["TLRL%015d" % len(filterTotal)]

  dstF = open (dstfilename, "w")
  dstF.writelines(finalLines)
  dstF.close()

def main():
  dupfile("src.P", "dst.P", 3)

if __name__ == '__main__':
    main()

#  =========================================================
#  src.P 样本文件
#  HEDR
#  SHDR
#  POSD
#  TLRL000000000000003
#  =========================================================
#  输出 dst.P
#  =========================================================
#  HEDR
#  SHDR
#  POSD
#  HEDR
#  SHDR
#  POSD
#  HEDR
#  SHDR
#  POSD
#  TLRL000000000000009
#  =========================================================