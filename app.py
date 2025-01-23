from flask import Flask 

app = Flask(__name__)

# create a idea repository, This where the ideas is stored
ideas = {
    1:{
        "id":1,
        "idea_name": "ONDC",
        "idea_description":"Details about ONDC",
        "idea_author":"Adeeb"
    },
    2:{
        "id":2,
        "idea_name": "Save Soil",
        "idea_description":"Details about saving soil",
        "idea_author":"Ankit Sharma"
    }
}

'''
Create an RESTful endpoint for fetching all the ideas
'''
@app.get("/ideaapp/api/v1/ideas")
def get_all_ideas():
    # logic to fetch all ideas
    return ideas


if __name__ == "__main__":
    app.run(port=9999)