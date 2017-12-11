#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import jieba
import jieba.analyse as analy
jieba.load_userdict("F:\\Development\\Code\\20171210\\user_dict.txt")
file=open("F:\\Development\\Code\\20171210\\simgle_news.txt","r")
stopwords = [line.strip() for line in open("F:\\Development\\Code\\20171210\\stop_word.txt", 'r').readlines()]
content = file.read()
##全模式
#word_list = jieba.cut(content,cut_all=True)
#print "全模式："," ".join(word_list)
#精确模式 , 默认就是精确模式
word_list = jieba.cut(content,cut_all=False)
outstr = ''
for word in word_list:
    if word not in stopwords:
        if word != '\t':
            outstr += word
            outstr += " "
print "精确模式："+outstr
##搜索引擎模式
#word_list = jieba.cut_for_search(content)
#print "搜索引擎："," ".join(word_list)

word_topk = analy.extract_tags(content,topK=5)
print "\n频率最高的词语："
print " ".join(word_topk)