import os

a = 2
print("coucou", a)

token = os.environ.get("SECRET_API_TOKEN")
if token == "42":
    print("Le script a bien recu le secret")
else:
    print("Secret absent")