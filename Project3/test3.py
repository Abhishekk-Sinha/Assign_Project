# 3. Implement OAuth2 authentication to allow users to log in using their Google or Facebook accounts


from flask import Flask, redirect, url_for, session, render_template
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = 'your_secret_key'

oauth = OAuth(app)

# Register Google OAuth
google = oauth.register(
    name='google',
    client_id='YOUR_GOOGLE_CLIENT_ID',
    client_secret='YOUR_GOOGLE_CLIENT_SECRET',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    refresh_token_url=None,
    refresh_token_params=None,
    redirect_uri='http://localhost:5000/google-callback',
    client_kwargs={'scope': 'openid profile email'}
)

# Register Facebook OAuth
facebook = oauth.register(
    name='facebook',
    client_id='YOUR_FACEBOOK_CLIENT_ID',
    client_secret='YOUR_FACEBOOK_CLIENT_SECRET',
    authorize_url='https://www.facebook.com/dialog/oauth',
    authorize_params=None,
    access_token_url='https://graph.facebook.com/oauth/access_token',
    access_token_params=None,
    refresh_token_url=None,
    refresh_token_params=None,
    redirect_uri='http://localhost:5000/facebook-callback',
    client_kwargs={'scope': 'email'}
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/google')
def login_google():
    return google.authorize_redirect(redirect_uri=url_for('google_callback', _external=True))

@app.route('/login/facebook')
def login_facebook():
    return facebook.authorize_redirect(redirect_uri=url_for('facebook_callback', _external=True))

@app.route('/google-callback')
def google_callback():
    token = google.authorize_access_token()
    user_info = google.parse_id_token(token)
    # Store user_info in the database or session
    return redirect(url_for('index'))

@app.route('/facebook-callback')
def facebook_callback():
    token = facebook.authorize_access_token()
    user_info = facebook.get('me?fields=id,email').json()
    # Store user_info in the database or session
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
