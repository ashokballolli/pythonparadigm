import json

applicants = """{
  "Scott C Aldridge": "Present",
  "Joe L Foss": "Present",
  "Clyde M Gold": "Present",
  "Monique C Doolittle": "Absent",
  "David M Volkert": "Present",
  "Israel M Oneal": "Present",
  "Elizabeth M Groff": "Absent"
}"""


def json_ops():
    applicants_json = json.loads(applicants)
    for key, value in applicants_json.items():
        print(key, value)

    swap_applicants_k_v = { v:k for k, v in applicants_json.items()}
    print(swap_applicants_k_v)

    values = applicants_json.values()
    print(values)


json_ops()