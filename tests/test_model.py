import pytest
import pandas as pd
from src.model import predict
import numpy as np
import os

class MockModel:
    def predict(self, data):
        return np.array([1.0] * len(data))

@pytest.fixture
def sample_model():
    model = MockModel()
    model_path = 'model.pkl'
    with open(model_path, 'wb') as file:
        import pickle
        pickle.dump(model, file)
    
    yield model

    # Cleanup
    os.remove(model_path)

def test_predict_valid_data(sample_model):
    valid_data = pd.DataFrame({
        '7-Day MA': [75.0, 76.0, 77.0]
    })
    
    predictions = predict(sample_model, valid_data)
    assert isinstance(predictions, np.ndarray), "As previsões devem ser um numpy.ndarray."
    assert len(predictions) == len(valid_data), "O número de previsões deve corresponder ao número de entradas."