from google.cloud import aiplatform
import time

def create_custom_job(
    date: str,
    project: str,
    display_name: str,
    container_image_uri: str,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com"
):
    """
    Creates custom training job
    
    Parameters
    ----------  
    date : str
        Format : '%Y-%m-%d'
    project : str
        Project name
    display_name : str
        Name of custom training job
    container_image_uri: str
        image_uri
    location : str
        Default: 'us-central1'
    api_endpoint : str
        api_endpoint option for Job Service Client
        
    Returns
    -------
    str
        Returns response of client.create_custom_job and executes the job in Vertex AI 
    """
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.JobServiceClient(client_options=client_options)
    custom_job = {
        "display_name": display_name + "_" + date,
        "job_spec": {
            "worker_pool_specs": [
                {
                    "machine_spec": {
                        "machine_type": "n1-standard-4",
                        "accelerator_type": aiplatform.gapic.AcceleratorType.NVIDIA_TESLA_K80,
                        "accelerator_count": 1,
                    },
                    "replica_count": 1,
                    "container_spec": {
                        "image_uri": container_image_uri,
                        "command": [],
                        "args": [],
                    },
                }
            ]
        },
    }
    parent = f"projects/{project}/locations/{location}"
    response = client.create_custom_job(parent=parent, custom_job=custom_job)
    time.sleep(600) 
    print("response:", response)
