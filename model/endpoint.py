from google.cloud import aiplatform

def model_endpoint(name,model,image,machine='n1-standard-4'):
    """
    Creates a model through Vertex AI and deploys it into an endpoint from Vertex AI
    
    Parameters
    ----------        
    name : str
        Name of the model in Vertex AI
    model : str
        Bucket path of model to deploy
    image: str
        Container image uri
    machine : str
        Default: 'n1-standard-4'
        
    Returns
    -------
    str
        Executes a model and an endpoint through Vertex AI 
    """
    model = aiplatform.Model.upload(
        display_name=name,
        artifact_uri=model,
        serving_container_image_uri=image)

    endpoint = model.deploy(
        machine_type=machine)
