from tqdm import tqdm
import random
import pandas as pd
from model import get_model
from data_loader import load_data
from util import transformers_logger


def predict(model, data):
    transformers_logger.info('------------------testing started----------------------')
    eval_len = len(data)
    transformers_logger.info(eval_len)
    seed = random.randint(1, 1000)
    transformers_logger.info(f'random seed is {seed}')
    random.seed = seed
    actual_titles = []
    actual_abstracts = []
    predict_titles = []
    for i in tqdm(range(1, min(1001, eval_len)), desc='collecting test inputs'):
        random_num = random.randint(1, eval_len)
        actual_titles.append(data.iloc[random_num]['target_text'])
        actual_abstracts.append("summarize: " + data.iloc[random_num]['input_text'])

    predict_titles = model.predict(actual_abstracts)

    predict_df = pd.DataFrame({
        'predict_title': predict_titles,
        'actual_title': actual_titles,
        'actual_abstract': actual_abstracts
    })

    predict_df.to_json('./data/predict_result.json', orient="split", index=False)
    transformers_logger.info('predicted file saved to ./data/predict_result.json')
    return predict_df


if __name__ == '__main__':
    train_df, eval_df, test_df = load_data()
    transformers_logger.info(train_df.shape, eval_df.shape, test_df.shape)
    model = get_model()
    predict_df = predict(model, test_df)
    transformers_logger.info(predict_df)
