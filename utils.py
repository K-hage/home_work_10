import json
# import urllib.request


def get_candidates():
    with open("candidate.json", encoding="utf-8") as file:
        return json.load(file)

# def get_images(image):
#     response = urllib.request.urlopen(image)
#     return response.geturl()
