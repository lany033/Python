filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = filenames.copy()
for index,files in enumerate(filenames):
    if "hpp" in files:
        i = files.index("hpp")
        newfile = files[0:i]+"h"
        newfilenames[index]=newfile

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]