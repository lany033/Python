wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for clothe,color in wardrobe.items():
	for item in color:
		print("{} {}".format(item,clothe))