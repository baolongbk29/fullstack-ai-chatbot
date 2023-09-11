import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()


class GPT2_Medium_VN:
    def __init__(self):
        self.url = os.environ.get("MODEL_URL")
        self.headers = {
            "Authorization": f"Bearer {os.environ.get('HUGGINFACE_INFERENCE_TOKEN')}"
        }
        self.payload = {
            "inputs": ""
        }

    def query(self, input: str) -> list:
        self.payload["inputs"] = input
        data = json.dumps(self.payload)
        response = requests.request(
            "POST", self.url, headers=self.headers, data=data)
        print(json.loads(response.content.decode("utf-8")))
        return json.loads(response.content.decode("utf-8"))


if __name__ == "__main__":
    GPT2_Medium_VN().query("Stocks rallied and the British pound gained.")
