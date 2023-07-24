import bcrypt

class User:
    def __init__(self):
        self.data = {}

    def __setattr__(self, name, value):
        # Store data in the dictionary, but avoid infinite recursion
        if name != 'data':
            self.data[name] = value
        else:
            # Call the base class's __setattr__ for 'data' attribute
            super().__setattr__(name, value)

    def __getattr__(self, name):
        return self.data.get(name, None)

    # def set_follower(self):
    #     self.follower =  1000 if self.follower == None else self.follower
    #     return self
    
    def follow(self):
        self.follower = 1
        self.following = 1
    

    def save(self):
        return self.data

# Usage
user = User()
user.name = 'John Doe'
user.age = 30

# user.follower = 100
user.follow()
result = user.save()

# Output the result as a dictionary
print(result)
