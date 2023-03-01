import requests

response = requests.get(
    url="https://ml-deployment-workshop-c6o7yruri-dominikriedermbw.vercel.app/",
    headers={
        "api-key": "my-secret-key"
    }
)

print(response.json())