from fastapi import FastAPI
from textblob import TextBlob
from pydantic import BaseModel

app = FastAPI()


class InputText(BaseModel):
    text: str


def sentiment_score(text: str) -> int:
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity
    # Normalize the sentiment to a 1-10 scale
    score = int((sentiment + 1) * 4.5) + 1
    return score


@app.post("/sentiment")
async def get_sentiment(input_text: InputText):
    score = sentiment_score(input_text.text)
    return {"sentiment_score": score}


@app.get("/")
def read_root():
    return {"message": "Hello World"}
