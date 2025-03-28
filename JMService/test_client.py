import requests
from requests_toolbelt.multipart import decoder

response = requests.post("http://localhost:8000/generate-pdf/", json=['1096392'])
multipart_data = decoder.MultipartDecoder.from_response(response)

for part in multipart_data.parts:
    filename = part.headers[b'Content-Disposition'].decode().split('filename="')[1][:-1]
    with open(filename, 'wb') as f:
        f.write(part.content)
    print(f"Saved: {filename}")
