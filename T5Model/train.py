import sys
from model import get_model
from data_loader import load_data
from util import transformers_logger


if __name__ == '__main__':
    train_df, eval_df, test_df = load_data()
    transformers_logger.info(train_df.shape, eval_df.shape, test_df.shape)
    model = get_model()
    model.train_model(train_df, eval_data=eval_df)
    test_result = model.eval_model(test_df)
    transformers_logger.info(test_result)
    if len(sys.argv) > 1:
        predict_arg = sys.argv[1]
        if predict_arg == 'predict':
            from T5Model.predict import predict
            predict_df = predict(model. test_df)
            transformers_logger.info(predict_df)