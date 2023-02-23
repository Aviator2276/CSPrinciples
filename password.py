website = input(str("What website will you be using this password for? "))
abbr = input(str("What is a two letter abbreviation for this website? "))
abbr.upper()
verb = input(str("What is a verb that describes how you use this website? "))
vowels = ["a","e","i","o","u"]
count = 0
verb2 = verb

for i in verb:
    for v in vowels:
        if v == verb[count]:
            verb2 = verb2.replace(verb[count], "")
    count = count + 1
print(verb2)