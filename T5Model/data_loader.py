from data_process import getpaper


def load_data():
    papers = getpaper()
    papers['prefix'] = "summarize"
    
    eval_df = papers.sample(frac=0.2, random_state=101)
    train_df = papers.drop(eval_df.index)
    test_df = eval_df.sample(frac=0.5, random_state=547)
    eval_df = eval_df.drop(test_df.index)

    return train_df, eval_df, test_df