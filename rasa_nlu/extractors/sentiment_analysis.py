from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from textblob import TextBlob
from typing import Any, Optional, Text

from rasa_nlu.components import Component
from rasa_nlu.model import Metadata
from rasa_nlu.training_data import TrainingData, Message


class SentimentAnalysis(Component):
    name = "sentiment_textblob"

    provides = ["sentiment"]

    def train(self, training_data, config, **kwargs):
        # type: (TrainingData) -> None

        pass

    def process(self, message, **kwargs):
        # type: (Message, **Any) -> None

        sentiment = get_sentiment(message.text)
        message.set("sentiment", sentiment,
                    add_to_output=True)


def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = 0.0
    subjectivity = 0.0
    for sentence in blob.sentences:
        sentiment += sentence.sentiment.sentiment
        subjectivity += sentence.sentiment.subjectivity

    if len(blob.sentences):
        return {
            "polarity": sentiment / len(blob.sentences),
            "subjectivity": subjectivity / len(blob.sentences)
        }
    else:
        return {
            "polarity": 0.0,
            "subjectivity": 0.0
        }
