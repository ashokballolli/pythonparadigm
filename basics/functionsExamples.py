def mean(mylist):
    mn = sum(mylist) / len(mylist)
    return mn


print(mean([1, 4, 7]))
print(type(mean), type(sum))


def meanAllType01(value):
    if type(value) == dict:
        mean = sum(value.values()) / len(value)
    else:
        mean = sum(value) / len(value)
    return mean

def meanAllType02(value):
    if isinstance(value, dict):
        mean = sum(value.values()) / len(value)
    else:
        mean = sum(value) / len(value)
    return mean

print(meanAllType01([1, 4, 7]))
dictInput = {'a': 3, 'b': 4, 'c': 5}
print(dictInput.values())
print(meanAllType01(dictInput))
print(meanAllType02(dictInput))



x=1
y=2
if x==1 and y==2:
    print("yes")
else:
    print("no")

def warmOrCold(temp):
    if temp < 7:
        print("Cold")
    elif temp == 7:
        print("Medium Temp")
    else:
        print("Warm")

warmOrCold(7)


# # Reading user inputs
#
# inpuTemp = input("Enter the temperature:\n")
# warmOrCold(inpuTemp)

# # String formatter
# inputName = input("Please enter your name: \n")
# message = f"Hi, {inputName}"
# print(message)
#

# Loop for iterating the dictonaries (keys, values, items)

contacts = {'Ashok': "323545354",
           'Arun': "98789",
           'Shilpa': "443222"}

for contact in contacts.items():
    print("{} contact number is {}".format(contact[0], contact[1]))

for name, number in contacts.items():
    print("{} contact number is {}".format(name, number))

for name in contacts.keys():
    print(name)