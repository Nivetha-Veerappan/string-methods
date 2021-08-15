//endswith
quote = "Smile"
x=quote.endswith("e")
print(x)

//isalnum
birthday =["1june']
x=birthday.isalnum()
print(x)

//joins
name = ["Silence", "is", "powerful"]
x= "*".join(name)
print(x) 

//make trans
text = "flower"
change = text.maketrans("w", "u")
print(text.translate(change))