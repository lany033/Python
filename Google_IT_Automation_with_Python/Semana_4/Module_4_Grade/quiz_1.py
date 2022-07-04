def format_address(address_string):
  # Declare variables
  address = address_string.split()
  number = []
  name = []
  new_address = []
  # Separate the address string into parts

  # Traverse through the address parts
  for e in address:
    # Determine if the address part is the
    # house number or part of the street name
    if e.isnumeric():
      number += e
    else:
      name += e
  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format("".join(number),"".join(name))

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))