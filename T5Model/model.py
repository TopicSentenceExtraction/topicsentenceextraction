from simpletransformers.t5 import T5Model


def get_model():
    model_args = {
        "reprocess_input_data": True,
        "overwrite_output_dir": True,
        "max_seq_length": 200,
        "train_batch_size": 16,
        "num_train_epochs": 10,
        "evaluate_during_training": True,
        "evaluate_during_training_steps": 500,
    }

    # Create T5 Model
    model = T5Model(model_name="t5-small", model_type='t5', args=model_args, use_cuda=True)

    return model