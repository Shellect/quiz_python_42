from fastapi import FastAPI

app = FastAPI()

@app.get("/question")
def get_question():
    return {
        "question" : "Зимой и летом одним цветом",
        "answers" : [
            "Елка",
            "Медведь",
            "Небо",
            "Охотник"
        ]
    }

@app.get("/health")
def get_service_health():
    return list()