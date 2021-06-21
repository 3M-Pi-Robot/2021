a = 7
b = 56.5
print(a)
print(b)
print(a+b)

print("----------------------------------")

c="Text"
print(c)

print("----------------------------------")

d = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(d)
print(d["year"])


print("----------------------------------")

e = ["Ford", "Volvo", "BMW","Mercedes"]
print(e)
print(e[0])
print(e[1])
print(e[2])
print(e[3])


print("----------------------------------")

f= [["Ford", "Volvo", "BMW"],["slow", "fast", "superfast"]]
print(f)
print(f[0])
print(f[0][1])
print(f[1])
print(f[1][1])


print("----------------------------------")

#print(a + c) # does not work!
print(str(a)+c)
print(a,c, "test")
