import bcrypt

class User:
    def __init__(self):
        self.data = {}

    def __setattr__(self, name, value):
        # Store data in the dictionary, but avoid infinite recursion
        print(name)
        if name != 'data':
            self.data[name] = value
        else:
            # Call the base class's __setattr__ for 'data' attribute
            super().__setattr__(name, value)

    def __getattr__(self, name):
        return self.data.get(name, None)

    def save(self):
        return self.data

# Usage
user = User()
user.name = 'John Doe'
user.age = 30

# Accessing the properties using __getattr__
print(user.name)  # Output: John Doe
print(user.age)   # Output: 30

result = user.save()

# Output the result as a dictionary
print(result)
