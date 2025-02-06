import dill

def load_pipeline():
    """Loads the serialized Pipeline"""
    model_path = '../../../ModelDevelopment/Final_model/pipeline.pk'
    with open(model_path, 'rb') as file:
        pipeline = dill.load(file)
    return pipeline