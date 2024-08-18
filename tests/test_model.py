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
    model_path = 'src/model.pkl'
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
    
    # Print the type and content of predictions
    print(f"Tipo de previsões: {type(predictions)}")
    print(f"Conteúdo das previsões: {predictions}")
    
    assert isinstance(predictions, pd.DataFrame), "As previsões devem ser um pandas.DataFrame."
    assert len(predictions) == len(valid_data), "O número de previsões deve corresponder ao número de entradas."

def test_predict_invalid_data(sample_model):
    invalid_data = pd.DataFrame({
        'Other Column': [1, 2, 3, 4, 5]
    })

    try:
        predict(sample_model, invalid_data)
    except ValueError as e:
        # Print the exception message
        print(f"Erro: {e}")
        raise e
