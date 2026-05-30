from pydantic import BaseModel,conint,constr


# class User(BaseModel):
#     id: int
#     name: str
#     age: int
#     email: str

# user = User(id=1, name='John Doe', age=30, email='john.doe@example.com')



# Modifying the previous model
class User(BaseModel):
    id: int
    name: str
    age: int = 0  # Default value if age is not provided
    email: str = "noemail@example.com" # Default value if email is not provided

# Create instances of User and print them
user1 = User(id=2, name="Jane Doe", email="janedoe@example.com")
print(user1)

user2 = User(id=3,name="Alice",age=25)
print(user2)


class another_user(BaseModel):
    id: conint(gt=0) #id must be greater than 0
    name: constr(min_length=2,max_length=50)

valid_user = another_user(id=1,name="Liridona")
print(valid_user)