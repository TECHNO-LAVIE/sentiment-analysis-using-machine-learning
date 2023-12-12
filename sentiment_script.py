from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float


def get_mood(input_text: str, *, treshold: float) -> Mood:
    sentiment: float = TextBlob(input_text).sentiment.polarity

    friendly_treshold: float = treshold
    hostile_treshold: float = -treshold

    if sentiment >= friendly_treshold:
        return Mood('☺️', sentiment)
    elif sentiment <= hostile_treshold:
        return Mood('😠', sentiment)
    else:
        return Mood('😑', sentiment)
    
if __name__ == '__main__':
    while True:
        text: str = input('Text:')
        mood: Mood = get_mood(text, treshold=0.3)

        print(f'{mood.emoji} ({mood.sentiment})')