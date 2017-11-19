#!/usr/bin/env python
# -*- coding:utf-8 -*-
filee = open("C:\\Users\\10673\\Desktop\\table_struct.txt", "r")
line_cnt=len(filee.readlines())
filee = open("C:\\Users\\10673\\Desktop\\table_struct.txt", "r")
print line_cnt
c1=filee.readline(line_cnt-5)
c2=filee.readline(line_cnt-8)
print c1
print c2
#import csv
#import codecs
#with open('C:\\Users\\10673\\Desktop\\struct.csv', 'wb') as csvfile:
#    spamwriter = csv.writer(csvfile, dialect='excel')
#    csvfile.write(codecs.BOM_UTF8)
#    file = open("C:\\Users\\10673\\Desktop\\table_struct.txt", "r")
#    db_name=""
#    table_name=""
#    line_n_1=""
#    line_n_2=""
#    line_n_3=""
#    spamwriter.writerow(['库名','表名','字段名','字段类型','注释'])
#    for line in file:
#        if line.isspace() == False:
#            if line.find("DB:") == -1:
#                if line.find("TABLE:") == -1:
#                     arrays=line.split("\t")
#                     arrays_with_head=[db_name,table_name]
#                     arrays_with_head.extend(arrays)
#                     spamwriter.writerow(arrays_with_head)
#                else:
#                    table_name=line.split(":")[1]
#            else:
#                db_name=line.split(":")[1]