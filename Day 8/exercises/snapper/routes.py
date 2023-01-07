from models import User, Post
from flask import Flask, render_template

app = Flask(__name__)

users = [
    User("Kieran", 
        "https://images.unsplash.com/photo-1624556664105-f1607ca6a2da?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1374&q=80",
        "https://images.unsplash.com/photo-1610222652439-74d502c89763?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1374&q=80",
        
        "Ad aliqua deserunt eu ullamco veniam excepteur cupidatat nostrud non. Sit proident elit excepteur mollit in dolore eiusmod nostrud fugiat labore. Sunt fugiat sint dolore excepteur ea voluptate pariatur exercitation duis ipsum consectetur. Aliquip ipsum elit voluptate fugiat sint excepteur Lorem Lorem aliqua ullamco consectetur laborum laboris. Est et magna cupidatat Lorem nisi ullamco.",
        [
            Post("Birb", "Look at him","https://images.unsplash.com/photo-1624556141200-e50559a7a647?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1374&q=80"),
            Post("Pinecone", "Very nature","https://images.unsplash.com/photo-1620144322949-29c9fee9094e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1374&q=80"),
            Post("Owl", "Hoo Hoo", "https://images.unsplash.com/photo-1624556314380-b35bd7896185?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1374&q=80")
        ]
    ),
    
    User("Jennifer", 
        "https://images.unsplash.com/photo-1623435151175-5e5d98bc1e8f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80",
        "https://images.unsplash.com/photo-1548267068-d1e0e8b1541c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80",
        
        "Ad aliqua deserunt eu ullamco veniam excepteur cupidatat nostrud non. Sit proident elit excepteur mollit in dolore eiusmod nostrud fugiat labore. Sunt fugiat sint dolore excepteur ea voluptate pariatur exercitation duis ipsum consectetur. Aliquip ipsum elit voluptate fugiat sint excepteur Lorem Lorem aliqua ullamco consectetur laborum laboris. Est et magna cupidatat Lorem nisi ullamco.",
        [
            Post("Pow", "Gnar","https://images.unsplash.com/photo-1609952769887-7905b6b02c0f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=688&q=80"),
            Post("Out of bounds", "Sick","https://images.unsplash.com/photo-1616429553002-faf23468952d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"),
            Post("That view", ";)", "https://images.unsplash.com/photo-1498576260462-eefc9d0ce9f7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1469&q=80")
        ]
    ),
    User("Megan", 
        "https://images.unsplash.com/photo-1434596922112-19c563067271?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80",
        "https://images.unsplash.com/photo-1544334845-576c8c7bb8ad?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
        
        "Ad aliqua deserunt eu ullamco veniam excepteur cupidatat nostrud non. Sit proident elit excepteur mollit in dolore eiusmod nostrud fugiat labore. Sunt fugiat sint dolore excepteur ea voluptate pariatur exercitation duis ipsum consectetur. Aliquip ipsum elit voluptate fugiat sint excepteur Lorem Lorem aliqua ullamco consectetur laborum laboris. Est et magna cupidatat Lorem nisi ullamco.",
        [
            Post("Won championships", "Pog","https://images.unsplash.com/photo-1526649307696-7c0518fbe422?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1430&q=80"),
            Post("Going climbing today", "Made it to the top!","https://images.unsplash.com/photo-1507034589631-9433cc6bc453?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=684&q=80"),
            Post("Ohmmm", "Happy place", "https://images.unsplash.com/photo-1506126613408-eca07ce68773?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=799&q=80")
        ]
    )
]

@app.route('/')
def index():
    return render_template("index.html")

#TODO: add /user/<id_number> route

if __name__ == '__main__':
    app.run(debug=True)
