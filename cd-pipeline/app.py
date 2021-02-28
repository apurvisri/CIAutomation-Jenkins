from flask import Flask, render_template
import random

app = Flask(__name__)

#List of earth images
images = [
    "https://media.giphy.com/media/UTqVVxyukfeiUZ9EDa/giphy.gif",
    "https://media.giphy.com/media/dSeSFmW5XAbYQIQIam/giphy.gif",
    "https://media.giphy.com/media/JidwhuCLt3u5sXimzc/giphy.gif",
    "https://media.giphy.com/media/xTg8AOrfulvLaGx39K/giphy.gif",
    "https://media.giphy.com/media/3o7WIB00yXujVt4WEo/giphy.gif",
    "https://media.giphy.com/media/1zlU57Bawc50fi3AwJ/giphy.gif",
    "https://media.giphy.com/media/4Nx9CO1QPZWuVSNSrG/giphy.gif",
    "https://media.giphy.com/media/3fibz5opL3jqrFgvXi/giphy.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
