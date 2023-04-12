import pytest
from main import sentiment_score


@pytest.mark.parametrize(
    "input_text,expected_score",
    [
        ("I love this!", 8),
        ("This is terrible.", 1),
        ("I don't know how I feel about this.", 5),
    ],
)
def test_sentiment_score(input_text, expected_score):
    score = sentiment_score(input_text)
    assert score >= expected_score
