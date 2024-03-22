# import the inference-sdk
from inference_sdk import InferenceHTTPClient

# initialize the client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="bJT1lGFWeDKlgSgbvg9j"
)

# infer on a local image
result = CLIENT.infer("a.jpg", model_id="brain-tumor-5na5y/1")


