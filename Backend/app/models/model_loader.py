import dill

def load_pipeline():
    """Loads the serialized Pipeline"""
    model_path = 'model_files/pipeline.pkl'
    with open(model_path, 'rb') as file:
        pipeline = dill.load(file)
    return pipeline