import pandas as np
import numpy as np

def model_predictor(sample, config):
    model = config["model"]
    sample = sample.values
    sample = np.expand_dims(sample, axis = 0)
    result = model.predict(sample)
    return result[0]