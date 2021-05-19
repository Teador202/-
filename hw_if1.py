def main(string_1, string_2):
    if type (string_1) == str and (string_2) == str:
        if len(string_1) == len(string_2):
            return 1
    elif len(string_1) > len(string_2) and len(string_1) != len(string_2):
        return 2
    elif len(string_1) != len(string_2) and len(string_2) == "learn":
        return 3
    else:
        return 0

print(main('le', '15'))
print(main('hello', 'hi'))
print(main('hi','learn'))

