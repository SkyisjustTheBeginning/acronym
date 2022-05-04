acronym = str(input("Sentence : "))
acronym_string = ""
v = acronym.split(" ")
for k in v:
   acronym_string += k[0]
   

print(acronym_string.upper())
