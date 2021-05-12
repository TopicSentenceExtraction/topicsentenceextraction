# -*- coding:utf-8 -*-
import logging
import numpy as np
import pandas as pd
import re
import json
from nltk.translate.bleu_score import corpus_bleu


def calculate_average(precisions, weights):
    """Calculate the geometric weighted mean."""
    tmp_res = 1
    for id, item in enumerate(precisions):
        tmp_res = tmp_res*np.power(item, weights[id])
    tmp_res = np.power(tmp_res, np.sum(weights))
    return tmp_res


def calculate_candidate(gram_list, candidate):
    """Calculate the count of gram_list in candidate."""
    gram_sub_str = ' '.join(gram_list)
    return len(re.findall(gram_sub_str, candidate))


def calculate_reference(gram_list, references):
    """Calculate the count of gram_list in references"""
    gram_sub_str = ' '.join(gram_list)
    gram_count = []
    for item in references:
        # calculate the count of the sub string
        gram_count.append(len(re.findall(gram_sub_str, item)))
    return gram_count


def bleu_v2(candidate_sentence, reference_sentences, max_gram, weights,mode=0):
    """
    https://en.wikipedia.org/wiki/BLEU
    bleu uses n-grams precision(usually 4)
    :return:
    """
    candidate_corpus = list(candidate_sentence.split(' '))
    # number of the reference sentences
    refer_len = len(reference_sentences)
    candidate_tokens_len = len(candidate_corpus)
    if mode == 0:
        gram_precisions= []
        for i in range(max_gram):
            # calculate each gram precision
            # set current gram length
            curr_gram_len = i+1
            # calculate current gram length mole
            curr_gram_mole = 0
            # calculate current gram length deno
            curr_gram_deno = 0
            for j in range(0, candidate_tokens_len, curr_gram_len):
                if j + curr_gram_len > candidate_tokens_len:
                    continue
                else:
                    curr_gram_list = candidate_corpus[j:j+curr_gram_len]
                    gram_candidate_count = calculate_candidate(curr_gram_list, candidate_sentence)
                    # print(' current gram candidate count')
                    # print(gram_candidate_count)
                    gram_reference_count_list = calculate_reference(curr_gram_list, reference_sentences)
                    # print(' current gram reference count list')
                    # print(gram_reference_count_list)
                    truncation_list = []
                    for item in gram_reference_count_list:
                        truncation_list.append(np.min([gram_candidate_count, item]))
                    curr_gram_mole += np.max(truncation_list)
                    curr_gram_deno += gram_candidate_count
            gram_precisions.append(curr_gram_mole/curr_gram_deno)

        average_res = calculate_average(gram_precisions, weights)
    # penalty on very short sentences
    bp = 1
    reference_len_list = [len(item.split(' ')) for item in reference_sentences]
    if candidate_tokens_len in reference_len_list:
        bp = 1
    else:
        if candidate_tokens_len < np.max(reference_len_list):
            bp = np.exp(1-(np.max(reference_len_list)/candidate_tokens_len))
    return bp*average_res


def main():
    # read test result json
    df = pd.read_json('./data/predict/predict2/test_predict.json', orient='split')
    # df.to_json('./data/test_result_columns.json', orient='split')
    predict_titles = df['predict_title'].to_list()
    actual_titles = df['actual_title'].to_list()
    bleu_list = []
    # one input and one output list
    n = len(predict_titles)
    for i in range(n):
        try:
            bleu_v2_score = bleu_v2(predict_titles[i], [actual_titles[i]], 1, weights=[1], mode=0)
        except:
            bleu_v2_score = 0
        finally:
            bleu_list.append(bleu_v2_score)
    df['bleu'] = bleu_list
    print(df)
    df.to_json('./data/predict/predict2/test_predict_columns.json', orient='split')


if __name__ == '__main__':
    # full bleu test on references and candidate
    main()
    # predict_sentence = 'how old is the man'
    # train_sentences = ['this is a dog and not is a cat', 'this is a cat and not is a dog', 'it is a dragon', 'i like play ball']
    # bleu_v2_score = bleu_v2(predict_sentence, train_sentences, 4, weights=[0.25, 0.25, 0.25, 0.25], mode=0)