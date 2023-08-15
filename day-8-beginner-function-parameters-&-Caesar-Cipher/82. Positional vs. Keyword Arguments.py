# Function with more than 1 input:
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# Calling greet_with() with position Arguments:

greet_with("Jack Bauer", "Nowhere")
#vs
greet_with("Nowhere", "Jack Bauer")

# Calling greet_with() with Keyword Arguments:
greet_with(location="Nowhere", name="Jack Bauer")

