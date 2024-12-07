# import os
# from flask import Flask, render_template, request, session, redirect
# from flask_cors import CORS
# from flask_migrate import Migrate
# from flask_wtf.csrf import CSRFProtect, generate_csrf
# from flask_login import LoginManager

# from .models import db, User
# from .api.user_routes import user_routes
# from .api.auth_routes import auth_routes
# from .api.business_routes import business_routes
# from .api.review_routes import review_routes
# from .api.tag_routes import tag_routes


# from .seeds import seed_commands

# from .config import Config

# app = Flask(__name__)

# # Setup login manager
# login = LoginManager(app)
# login.login_view = 'auth.unauthorized'


# @login.user_loader
# def load_user(id):
#     return User.query.get(int(id))


# # Tell flask about our seed commands
# app.cli.add_command(seed_commands)

# app.config.from_object(Config)
# app.register_blueprint(user_routes, url_prefix='/api/users')
# app.register_blueprint(auth_routes, url_prefix='/api/auth')
# app.register_blueprint(business_routes, url_prefix="/api/businesses")
# app.register_blueprint(review_routes, url_prefix="/api/reviews")
# app.register_blueprint(tag_routes, url_prefix="/api/tags")
# db.init_app(app)
# Migrate(app, db)

# # Application Security
# CORS(app)


# # Since we are deploying with Docker and Flask,
# # we won't be using a buildpack when we deploy to Heroku.
# # Therefore, we need to make sure that in production any
# # request made over http is redirected to https.
# # Well.........
# @app.before_request
# def https_redirect():
#     if os.environ.get('FLASK_ENV') == 'production':
#         if request.headers.get('X-Forwarded-Proto') == 'http':
#             url = request.url.replace('http://', 'https://', 1)
#             code = 301
#             return redirect(url, code=code)


# @app.after_request
# def inject_csrf_token(response):
#     response.set_cookie(
#         'csrf_token',
#         generate_csrf(),
#         secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
#         samesite='Strict' if os.environ.get(
#             'FLASK_ENV') == 'production' else None,
#         httponly=True)
#     return response


# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def react_root(path):
#     if path == 'favicon.ico':
#         return app.send_static_file('favicon.ico')
#     return app.send_static_file('index.html')

import os
import requests
from flask import Flask, request, redirect, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager

from .models import db, User
from .api.user_routes import user_routes
from .api.auth_routes import auth_routes
from .api.business_routes import business_routes
from .api.review_routes import review_routes
from .api.tag_routes import tag_routes

from .seeds import seed_commands
from .config import Config

app = Flask(__name__)

# Setup login manager
login = LoginManager(app)
login.login_view = 'auth.unauthorized'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# Tell flask about our seed commands
app.cli.add_command(seed_commands)

app.config.from_object(Config)
app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(business_routes, url_prefix="/api/businesses")
app.register_blueprint(review_routes, url_prefix="/api/reviews")
app.register_blueprint(tag_routes, url_prefix="/api/tags")
db.init_app(app)
Migrate(app, db)

# Application Security
CORS(app, resources={r"/*": {"origins": "*"}})

# Redirect HTTP to HTTPS in production
@app.before_request
def https_redirect():
    if os.environ.get('FLASK_ENV') == 'production':
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)


@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    if path == 'favicon.ico':
        return app.send_static_file('favicon.ico')
    return app.send_static_file('index.html')


@app.route('/api/search-restaurants', methods=['GET'])
def search_restaurants():
    pin_code = request.args.get('pin_code')
    print(f"Received PIN code: {pin_code}")  # Log the received PIN code

    if not pin_code:
        return jsonify({"error": "PIN code is required"}), 400

    try:
        # Step 1: Fetch coordinates from Nominatim
        nominatim_endpoint = f"https://nominatim.openstreetmap.org/search?format=json&q={pin_code}"
        print(f"Nominatim URL: {nominatim_endpoint}")
        nominatim_response = requests.get(nominatim_endpoint).json()

        if len(nominatim_response) == 0:
            return jsonify({"error": "Location not found"}), 404

        location = nominatim_response[0]
        latitude = location['lat']
        longitude = location['lon']
        print(f"Coordinates: {latitude}, {longitude}")

        # Step 2: Fetch restaurants from Overpass API
        overpass_endpoint = (
            f"https://overpass-api.de/api/interpreter?data="
            f"[out:json];node[amenity=restaurant](around:5000,{latitude},{longitude});out;"
        )
        print(f"Overpass URL: {overpass_endpoint}")
        overpass_response = requests.get(overpass_endpoint).json()

        # Step 3: Extract restaurant data
        restaurants = overpass_response.get("elements", [])
        if not restaurants:
            return jsonify({"error": "No restaurants found nearby"}), 404

        return jsonify({"restaurants": restaurants})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)