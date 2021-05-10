import torch
import numpy as np
import json
import pandas as pd
import os
import re
import psutil
from util import print_run_time, transformers_logger

data_root = '../data/arxiv-metadata-oai-snapshot.json'


def get_data():
    with open(data_root, 'r') as f:
        for line in f:
            yield line


def cpu_stats():
    pid = os.getpid()
    py = psutil.Process(pid)
    memory_use = py.memory_info()[0] / 2. ** 30
    return 'Available RAM (GB):' + str(np.round(memory_use, 2))


# 基础preprocess
def basic_word_treatment(word):
    return re.sub(' +', ' ', re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]|\\$.*?$|\\<.*?>", "", word.replace('\n', ' ').replace('"','').strip()))


'''
测试数据集格式，将标题（title）和正文（abstract）从json文件中提取出来

'''
def sample_print(metadata):
    transformers_logger.info('-------------------------------------')
    transformers_logger.info('sample abstract and title shown below')
    for paper in metadata:
        paper_dict = json.loads(paper)
        transformers_logger.info('Title: {}\n\nAbstract: {}\nRef: {}'.format(basic_word_treatment(paper_dict.get('title')), basic_word_treatment(paper_dict.get('abstract')), paper_dict.get('journal-ref')))
    #     print(paper)
        break
    transformers_logger.info('-------------------------------------')


@print_run_time
def getpaper(metadata=None):
    titles = []
    abstracts = []
    years = []
    if not metadata:
        metadata = get_data()
    for paper in metadata:
        paper_dict = json.loads(paper)
        ref = paper_dict.get('journal-ref')  #引用
        try:
            year = int(ref[-4:])
            # from 2010 to 2021(both end included)
            if 2010 <= year <= 2021:
                years.append(year)
                titles.append(basic_word_treatment(paper_dict.get('title')))
                abstracts.append(basic_word_treatment(paper_dict.get('abstract')))
        except:
            pass

    papers = pd.DataFrame({
        'title': titles,
        'abstract': abstracts,
    })

    # print(getpaper().head())
    del titles, abstracts, years

    papers = papers[['title','abstract']]
    papers.columns = ['target_text', 'input_text']
    papers = papers.dropna()

    return papers


if __name__ == '__main__':
    metadata = get_data()
    # print(cpu_stats())
    sample_print(metadata)

