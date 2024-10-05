# import the inference-sdk
from inference_sdk import InferenceHTTPClient

# initialize the client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="ghzpyenPcNlDg1p1yWq9"
)

# infer on a local image
result = CLIENT.infer("./.jpg", model_id="departing.earth-dqxez/5")