import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import exc
import json
from models import setup_db, Assign, Movie, Actor, db_drop_and_create_all
from auth.auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    return app


app = create_app()
# db_drop_and_create_all()
'''
GET /movies
'''


@app.route('/movies')
@requires_auth('view:movies')
def retrieve_movies():

    selection = Movie.query.order_by(Movie.id).all()

    movies = [movie.format() for movie in selection]

    return jsonify({
        'success': True,
        'movies': movies,
    })


'''
POST /movies
'''


@app.route('/movies', methods=['POST'])
@requires_auth('add:movie')
def create_movie():

    body = request.get_json()

    new_title = body.get('title', None)
    new_release_date = body.get('release_date', None)
    new_boxoffice = body.get('boxoffice', None)

    try:
        movie = Movie(
                        title=new_title,
                        release_date=new_release_date,
                        boxoffice=new_boxoffice,
                        )
        movie.insert()

        selection = Movie.query.filter(Movie.id == movie.id)

        movie = [movie.format() for movie in selection]

        return jsonify({
            'success': True,
            'movie': movie,
        })

    except BaseException:
        abort(422)


'''
PATCH /movies
'''


@app.route('/movies/<int:movie_id>', methods=['PATCH'])
@requires_auth('modify:movie')
def patch_movies(movie_id):

    body = request.get_json()

    update_title = body.get('title', None)
    update_release_date = body.get('release_date', None)
    update_boxoffice = body.get('boxoffice', None)

    try:
        movie = Movie.query.filter(Movie.id == movie_id) \
                .one_or_none()

        if movie is None:
            abort(404)

        movie.title = update_title
        movie.release_date = update_release_date
        movie.boxoffice = update_boxoffice
        movie.update()

        selection = Movie.query.filter(Movie.id == movie.id)

        movie = [movie.format() for movie in selection]

        return jsonify({
            'success': True,
            'movie': movie
        })

    except BaseException:
        abort(400)


'''
DELETE /movies
'''


@app.route('/movies/<int:movie_id>', methods=['DELETE'])
@requires_auth('delete:movie')
def delete_movies(movie_id):

    try:
        movie = Movie.query.filter(Movie.id == movie_id) \
                .one_or_none()

        if movie is None:
            abort(404)

        movie.delete()

        return jsonify({
            'success': True,
            'delete': movie.id
        })

    except BaseException:
        abort(400)


'''
GET /actors
'''


@app.route('/actors')
@requires_auth('view:actors')
def retrieve_actors():

    selection = Actor.query.order_by(Actor.id).all()

    actors = [actor.format() for actor in selection]

    return jsonify({
        'success': True,
        'actors': actors,
    })


'''
POST /actors
'''


@app.route('/actors', methods=['POST'])
@requires_auth('add:actor')
def create_actor():

    body = request.get_json()

    new_name = body.get('name', None)
    new_age = body.get('age', None)
    new_gender = body.get('gender', None)

    try:
        actor = Actor(
                        name=new_name,
                        age=new_age,
                        gender=new_gender,
                        )
        actor.insert()

        selection = Actor.query.filter(Actor.id == actor.id)

        actor = [actor.format() for actor in selection]

        return jsonify({
            'success': True,
            'actor': actor,
        })

    except BaseException:
        abort(422)


'''
PATCH /actors
'''


@app.route('/actors/<int:actor_id>', methods=['PATCH'])
@requires_auth('modify:actor')
def patch_actors(actor_id):

    body = request.get_json()

    update_name = body.get('name', None)
    update_age = body.get('age', None)
    update_gender = body.get('gender', None)

    try:
        actor = Actor.query.filter(Actor.id == actor_id) \
                .one_or_none()

        if actor is None:
            abort(404)

        actor.name = update_name
        actor.age = update_age
        actor.gender = update_gender
        actor.update()

        selection = Actor.query.filter(Actor.id == actor.id)

        actor = [actor.format() for actor in selection]

        return jsonify({
            'success': True,
            'actor': actor
        })

    except BaseException:
        abort(400)


'''
DELETE /actors
'''


@app.route('/actors/<int:actor_id>', methods=['DELETE'])
@requires_auth('delete:actor')
def delete_actors(actor_id):

    try:
        actor = Actor.query.filter(Actor.id == actor_id) \
                .one_or_none()

        if actor is None:
            abort(404)

        actor.delete()

        return jsonify({
            'success': True,
            'delete': actor.id
        })

    except BaseException:
        abort(400)


'''
GET /assigns
'''


@app.route('/assigns')
@requires_auth('view:assign')
def retrieve_assigns():

    selection = Assign.query.order_by(Assign.id).all()

    assigns = [assign.format() for assign in selection]

    return jsonify({
        'success': True,
        'assigns': assigns,
    })


'''
POST /assigns
'''


@app.route('/assigns', methods=['POST'])
@requires_auth('add:assign')
def create_assign():

    body = request.get_json()

    new_movie_id = body.get('movie_id', None)
    new_actor_id = body.get('actor_id', None)

    try:
        assign = Assign(
                        movie_id=new_movie_id,
                        actor_id=new_actor_id,
                        )
        assign.insert()

        selection = Assign.query.filter(Assign.id == assign.id)

        assign = [assign.format() for assign in selection]

        return jsonify({
            'success': True,
            'assign': assign,
        })

    except BaseException:
        abort(422)


'''
DELETE /assigns
'''


@app.route('/assigns/<int:assign_id>', methods=['DELETE'])
@requires_auth('delete:assign')
def delete_assigns(assign_id):

    try:
        assign = Assign.query.filter(Assign.id == assign_id) \
                .one_or_none()

        if assign is None:
            abort(404)

        assign.delete()

        return jsonify({
            'success': True,
            'delete': assign.id
        })

    except BaseException:
        abort(400)


'''
Error Handling
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False,
                    "error": 422,
                    "message": "unprocessable"
                    }), 422


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400


@app.errorhandler(405)
def not_allowed(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": "method not allowed"
    }), 405


@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "server error"
    }), 500


# @app.errorhandler(AuthError)
# def auth_error(ex):
#     return jsonify({
#         "success": False,
#         "error": ex.status_code,
#         "message": ex.error['code']
#         }),  ex.status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
