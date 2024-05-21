# Isomorphics strings

a = "egg"
b = "add"
is_isomorphic = False

string1 = a[0].replace(a[0], b[0]) + a[1:].replace(a[1:], b[1] * 2)
string2 = b[0].replace(b[0], a[0]) + b[1:].replace(b[1:], a[1] * 2)

print(f"String 1: {string1}, String2: {string2}")


if string1 == b and string2 == a:
    is_isomorphic = True
    print(is_isomorphic)
else:
    print(is_isomorphic)
