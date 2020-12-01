#####################将政策文件中的内容抽取出来：标准、伦理、 3部分内容##########################
###########step 1：把3部分内容找到近义词，组成一个词表######
###########step 2：把文件与词表相匹配，判断文件到底在讲啥######
from nltk.corpus import wordnet as wn
import os
import codecs
# goods = wn.synsets('beautiful')
# beautifuls = wn.synsets('pretty')
# bads = wn.synsets('standard')

# print('good和bad的语义相似度为： ', max([0 if good.path_similarity(bad) == None else good.path_similarity(bad) for good in goods for bad in bads]))
def readOnePolicy(path2):
    ethic_set = wn.synsets('ethic')
    # print('ethic的同义词集为：', ethic_set)
    # print('ethic的各同义词集包含的单词有：', [ethic.lemma_names() for ethic in ethic_set])
    # print('ethic的各同义词集的具体定义是：',[dog.definition() for dog in ethic_set])
    # print('ethic的各同义词集的例子是：',[dog.examples() for dog in ethic_set])
    standard_set = wn.synsets('standard')
    privacy_set = wn.synsets('privacy')
    education_set = wn.synsets('education')
    investment_set = wn.synsets('investment')
    application_set = wn.synsets('application')
    content=''
    # with open(path2,'r',encoding='UTF-8') as f1:
    # with open(path2, 'r', encoding='UTF-8') as f1:
    with codecs.open(path2, 'r', encoding=u'utf-8', errors='ignore') as fr:###这里用codecs防止编码出错
        content=fr.read()
    content=content.split()
    # print(type(content))

    # content = wn.synsets('standard')

    # print('good和beautiful的语义相似度为： ', max([0 if one_ethic.path_similarity(one_word) == None else one_ethic.path_similarity(one_word) for one_ethic in ethic_set for one_word in content]))
    #
    # for ethic in ethic_set:
    #     # print(type(ethic.lemma_names()))##list
    #     for one_word in range(len(ethic.lemma_names())):
    #         print(ethic.lemma_names()[one_word])
    # print('content和ethic的语义相似度为： ', max([0 if good.path_similarity(beautiful) == None else good.path_similarity(beautiful) for good in goods for beautiful in beautifuls]))
    stop_words=''
    with open('stopWords.txt','r') as f2:
        stop_words=f2.read()
        stop_words=stop_words.split()

    ethic_max_prob = 0
    standard_max_prob = 0
    privacy_max_prob = 0
    education_max_prob = 0
    investment_max_prob = 0
    application_max_prob = 0
    for i in range(len(content)):
        contentSyns=[]
        if content[i] not in stop_words:
            if not content[i].isnumeric():
                # print(content[i],'   content[i]')
                contentSyns=wn.synsets(content[i])
                # print(contentSyns,'   contentsyns')###contentSyns有些是空的[]，下面max()会报错
                if len(contentSyns)>0:
                    ethic_prob=max([0 if e.path_similarity(c) == None else e.path_similarity(c) for e in ethic_set for c in contentSyns])
                    standard_prob = max([0 if s.path_similarity(c) == None else s.path_similarity(c) for s in standard_set for c in contentSyns])
                    privacy_prob = max([0 if p.path_similarity(c) == None else p.path_similarity(c) for p in privacy_set for c in contentSyns])
                    education_prob = max([0 if edu.path_similarity(c) == None else edu.path_similarity(c) for edu in education_set for c in contentSyns])
                    investment_prob = max([0 if i.path_similarity(c) == None else i.path_similarity(c) for i in investment_set for c in contentSyns])
                    application_prob = max([0 if a.path_similarity(c) == None else a.path_similarity(c) for a in application_set for c in contentSyns])

                    if ethic_prob>ethic_max_prob:
                        ethic_max_prob=ethic_prob
                    if standard_prob>standard_max_prob:
                        standard_max_prob=standard_prob
                    if privacy_prob>privacy_max_prob:
                        privacy_max_prob=privacy_prob
                    if education_prob > education_max_prob:
                        education_max_prob = education_prob
                    if investment_prob > investment_max_prob:
                        investment_max_prob = investment_prob
                    if application_prob > application_max_prob:
                        application_max_prob = application_prob


                    # print(max_prob,'   概率')

    # print(ethic_max_prob,'   ethic_max_prob')
    # print(standard_max_prob,'    standard_max_prob')
    # print(privacy_max_prob,'    privacy_max_prob')
    print(path2,'   ',ethic_max_prob,'   ',standard_max_prob,'   ',privacy_max_prob,'   ',education_max_prob,'   ',investment_max_prob,'   ',application_max_prob)

file_dir = r"txt"
for root, dirs, files in os.walk(file_dir):
    for f in range(len(files)):
        path1=os.path.join(file_dir,files[f])
        # print(path1,'    doc_name')
        readOnePolicy(path1)
        # with open(path1, 'r') as f1:
        #     content = f1.read()


