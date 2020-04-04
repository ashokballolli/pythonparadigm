import mysql.connector

connection = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

def translate(userInput):
    dbResult = getDbResult(userInput)
    if len(dbResult) > 0:
        return dbResult
    else:
        return "No results found"

def getDbResult(userInput):
    cursor = connection.cursor()
    execute = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % userInput)
    result = cursor.fetchall()
    return result


userInput = input("Enter a word: ")
result = translate(userInput)

if isinstance(result, list):
    for item in result:
        print(item[1])
else:
    print("No results found for your input")