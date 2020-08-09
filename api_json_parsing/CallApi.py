import requests
import json


# http://www.compjour.org/tutorials/intro-to-python-requests-and-json/
def get_github_status():
    github_status_url = "https://kctbh9vrtdwd.statuspage.io/api/v2/status.json"

    resp = requests.get(github_status_url)
    print(resp)  # <Response [200]>
    print(type(resp))  # <class 'requests.models.Response'>
    print(resp.text)
    print(resp.status_code)  # 200
    print(resp.ok)  # True
    print(resp.headers)
    print(resp.headers['Content-Type'])

    resp_json = resp.json()

    print(resp_json['page']['name'])  # GitHub
    print(resp_json['page']['url'])  # https://www.githubstatus.com


# Python to JSON (Encoding)
# dumps()	encoding to JSON objects
# dump()	encoded string writing on file
# JSON to Python (Decoding)
# loads()	Decode the JSON string
# load()	Decode while JSON file read

def encoding_using_dumps():
    # Converting Python data to JSON is called an Encoding operation. Encoding is done with the help of JSON library method – dumps()
    #
    # dumps() method converts dictionary object of python into JSON string data format.
    x = {
        "name": "Ken",
        "age": 45,
        "married": True,
        "children": ("Alice", "Bob"),
        "pets": ['Dog'],
        "cars": [
            {"model": "Audi A1", "mpg": 15.1},
            {"model": "Zeep Compass", "mpg": 18.1}
        ]
    }

    sorted_string = json.dumps(x, indent=4, sort_keys=True)
    print(type(sorted_string))  # <class 'str'>
    print(sorted_string)


def encoded_string_writing():
    # Let's create a JSON file of the dictionary using the function dump()
    x = {
        "name": "Ken",
        "age": 45,
        "married": True,
        "children": ("Alice", "Bob"),
        "pets": ['Dog'],
        "cars": [
            {"model": "Audi A1", "mpg": 15.1},
            {"model": "Zeep Compass", "mpg": 18.1}
        ]
    }
    with open("json_file.json", "w") as fp:
        json.dump(x, fp, indent=4, sort_keys=True)


def decoding_json_string():
    # JSON string decoding is done with the help of inbuilt method loads()
    # https://www.guru99.com/python-json.html
    text = """
        {"page":{"id":"kctbh9vrtdwd","name":"GitHub","url":"https://www.githubstatus.com","time_zone":"Etc/UTC","updated_at":"2020-08-09T08:19:28.373Z"},"status":{"indicator":"none","description":"All Systems Operational"}}
        """

    dict_obj = json.loads(text)

    print(type(dict_obj))  # <class 'dict'>
    print(dict_obj['page']['name'])  # GitHub
    # OR
    print(dict_obj.get('page').get('name'))  # GitHub
    print(dict_obj['page']['url'])  # https://www.githubstatus.com


def decoding_json_file():
    # Decoding JSON File or Parsing JSON file in Python
    file_data = ''
    try:
        with open("json_file.json", "r") as fp:
            file_data = json.load(fp)
    except FileNotFoundError as err:
        print("File not found ", str(err))
    except ValueError as err:
        print("Bad JSON file format,  Change JSON File", str(err))

        # if file_data:
    print(file_data)


# get_github_status()
# serialize_json()
# encoding_using_dumps()
# encoded_string_writing()
# decoding_json_string()
decoding_json_file()
