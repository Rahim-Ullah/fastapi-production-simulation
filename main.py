# basic api just to test in production (render)
from fastapi import FastAPI


app = FastAPI()

@app.get("/home")
def home():
    return {
        "Welcome :": "To testing in production tutorial!"
    }


# users route
@app.get("/users")
def get_users():
    return {
        "user1": {"Name: ": "Rahim Ullah", "Age": 22, "ID": 1}
        "user2": {"Name: ": "Abaseen", "Age": 23, "ID": 2}
        "user3": {"Name: ": "Salman", "Age": 21, "ID": 3}
    }