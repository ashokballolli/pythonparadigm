import json


def filter_names():
    x = """
        [
            {
                "type": 1,
                "name": "name 1"
            },
            {
                "type": 2,
                "name": "name 2"
            },
            {
                "type": 1,
                "name": "name 3"
            }
        ]
        """

    x_json = json.loads(x)
    # get all the names
    names = [x['name'] for x in x_json]
    print(names)

    # filter all the nodes of type = 1

    type01 = [x for x in x_json if x['type'] == 1]
    print(type01)



filter_names()
