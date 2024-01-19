def line(katz_deli):
    if katz_deli:
        line_string = "The line is currently:"
        for index, name in enumerate(katz_deli, start=1):
            line_string += f" {index}. {name}"
        print(line_string)
    else:
        print("The line is currently empty.")

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(katz_deli):
    if katz_deli:
        serving_name = katz_deli.pop(0)
        print(f"Currently serving {serving_name}.")
    else:
        print("There is nobody waiting to be served.")

katz_deli = []

take_a_number(katz_deli, "Ada")
take_a_number(katz_deli, "Grace")
take_a_number(katz_deli, "Kent")

line(katz_deli)

now_serving(katz_deli)

line(katz_deli)