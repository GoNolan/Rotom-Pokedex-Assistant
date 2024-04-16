import os

from flask import Flask, redirect, render_template, request, url_for
from openai import OpenAI
client = OpenAI(
  api_key=os.environ.get(".env")
)

app = Flask(__name__)

@app.route("/", methods=("GET", "POST"))
def index():
  if request.method == "POST":
    answer = request.form["answer"]
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {
        "role": "system", "content": "You are a helpful reference for users looking to understand the mechanics of Pokémon battles in the Pokémon games. Users will include information about the Pokémon they are using, including their name, level and typing, and will do the same for their opponent. You are to give the user feedback  about how whether or not they are likely to win. You should be specific about if the user needs to level up their Pokémon, and if their Pokémon is a good fit to take part in the battle based on their typing. Regardless, you will inform them about what Pokémon types are a good match against the Pokémon they are facing. Assume that the user is young and  inexperienced, so your tone should be helpful and supportive."
        },
        {"role": "user", "content": answer}
      ],
    )
    return redirect(url_for("index", result=response.choices[0].message.content))

  result = request.args.get("result")
  return render_template("index.html", result=result)