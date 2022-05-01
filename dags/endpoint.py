from google.cloud import aiplatform
from google.oauth2 import service_account

def model_endpoint(date,name,model,image,auth,machine='n1-standard-4'):
    """
    Creates a model through Vertex AI and deploys it into an endpoint from Vertex AI
    
    Parameters
    ----------   
    date : str
        Format : '%Y-%m-%d'
    name : str
        Name of the model in Vertex AI
    model : str
        Bucket path of model to deploy
    image: str
        Container image uri
    auth: str
    	Path to google cloud credentials
    machine : str
        Default: 'n1-standard-4'
        
    Returns
    -------
    str
        Executes a model and an endpoint through Vertex AI 
    """
    credentials = service_account.Credentials.from_service_account_file(auth)
    aiplatform.init(credentials=credentials)
    model = aiplatform.Model.upload(
        display_name=name + "_" + date,
        artifact_uri=model,
        serving_container_image_uri=image)

    endpoint = model.deploy(
        machine_type=machine)
