# Sentiment Analysis FastAPI App built with GPT4 and AWS AppRunner

This is a simple FastAPI app that takes a string as input and returns a sentiment score from 1 (negative) to 10 (positive) using TextBlob for sentiment analysis.

## Installation

Make sure you have Python 3.7 or higher installed.

1. Install the required packages:

```bash
pip install fastapi uvicorn textblob httpx pytest
```

2. Clone the repository or deploy it to AWS AppRunner as shown in this video.


## **Running the app**

Start the app by running:

```
uvicorn main:app --host 0.0.0.0 --port 8080
```

The app will be available at **`http://127.0.0.1:8080`**.


## **API Endpoints**

### **`/sentiment` (POST)**

Takes a JSON payload with a "text" field and returns the sentiment score.

Example request:

```json
{
  "text": "I love this!"
}
```

Example response:

```json
{
  "sentiment_score": 10
}

```

## **Testing**

To run the tests, execute:

```
pytest test_app.py
# or just
pytest
```

## **License**

This project is licensed under the Apache License.

## **Acknowledgments**

- **[FastAPI](https://fastapi.tiangolo.com/)**
- **[TextBlob](https://textblob.readthedocs.io/)**

