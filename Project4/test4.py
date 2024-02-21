# 4. Develop a recommendation system using Flask that suggests content to users based on their preferences.

from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy recommendation function
def recommend_items(user_id):
    # Replace this with your recommendation algorithm
    recommended_items = ["Item 1", "Item 2", "Item 3"]
    return recommended_items

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = request.form['user_id']
    recommended_items = recommend_items(user_id)
    return render_template('recommendation.html', items=recommended_items)

if __name__ == '__main__':
    app.run(debug=True)
