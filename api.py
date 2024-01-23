from flask import Flask, jsonify
from flask_cors import CORS
import random

quotes = [
    {
        "quoteText": "You know, Hobbes, some days even my lucky rocket ship underpants don't help.",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "What a stupid world",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "Everybody seeks happiness! Not me, though! That's the difference between me and the rest of the world. Happiness isn't good enough for me! I demand euphoria!",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "I think night time is dark so you can imagine your fears with less distraction.",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "As you can see, I have memorized this utterly useless piece of information long enough to pass a test question. I now intend to forget it forever. You've taught me nothing except how to cynically manipulate the system. Congratulations.",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "Van Gogh would've sold more than one painting if he'd put tigers in them.",
        "quoteAuthor": "Hobbes"
    },
    {
        "quoteText": "The world bores you when you're cool.",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "Isn't it strange that evolution would give us a sense of humour? When you think about it, it's weird that we have a physiological response to absurdity. We laugh at nonsense. We like it. We think it's funny. Don't you think it's odd that we appreciate absurdity? Why would we develop that way? How does it benefit us?",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "I suppose if we couldn't laugh at things that don't make sense, we couldn't react to a lot of life. I can't tell if that's funny or really scary.",
        "quoteAuthor": "Hobbes and Calvin"
    },
    {
        "quoteText": "Life is full of surprises, but never when you need one.",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "Getting an inch of snow is like winning 10 cents in the lottery.",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "People always make the mistake of thinking art is created for them. But really, art is a private language for sophisticates to congratulate themselves on their superiority to the rest of the world. As my artist's statement explains, my work is utterly incomprehensible and is therefore full of deep significance.",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "Verbing weirds language.",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "They say the world is a stage. But obviously the play is unrehearsed and everybody is ad-libbing his lines.Maybe that's why it's hard to tell if we're living in a tragedy or a farce.We need more special effects and dance numbers.",
        "quoteAuthor": "Calvin and Hobbes"
    },
    {
        "quoteText": "Sometimes I think the surest sign that intelligent life exists elsewhere in the universe is that none of it has tried to contact us.",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "So the secret to good self-esteem is to lower your expectations to the point where they're already met?",
        "quoteAuthor": "Hobbes"
    }, 
]

app = Flask(__name__)
CORS(app)
@app.route('/api/quotes/random')

def generate_random_quote():
    quote = random.choice(quotes)
    return jsonify(quote)

#the json will run on "http://127.0.0.1:8080/api/quotes/random"
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)

