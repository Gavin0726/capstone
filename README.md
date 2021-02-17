# Capstone Backend

## Getting Started

### Installing Dependencies

#### Python 3.8

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/starter` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.


### Application URL and Tokens

- URL:

https://capstone-gavin.herokuapp.com/


- Tokens:

ASSISTANT=
            'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkRGbEdBODQ5X0dsSjlJc0EycTQ4ciJ9.eyJpc3MiOiJodHRwczovL2dhdmluZ3VvLmF1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDJiMTU4YmRlNTViYzAwNmZjMzc1ZTciLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYxMzYwMjIzMiwiZXhwIjoxNjEzNjg4NjMyLCJhenAiOiJlVTJwNnpVZWliTHF0Z2l6d0JncnFlZWhaaHN5SEozMSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsidmlldzphY3RvcnMiLCJ2aWV3Om1vdmllcyJdfQ.A46JefmyOYXRVpyQGCHMS37xBnN3WQXpboBA47Q9Hriv0HQFYgzvKOhc1L3Obirw9rqxRXEiJ7hibddFxbekcUabCvibUJBKnUxNMAI6N-V3eGFFcIHg1DmrGL0xmcdptlELruK_vW4xIl7w_g9jhbksluR4Gb96rDTLPgz4DqdGleEHsATCxEIIOZPsZQLTHxzolHWouDqz65tJIcgGVwEOuRgkLWgc7XrT1vzRoHb6AknBpCcdctqUdyyUICf8RbySoJWWNaH3bocF7i9yOCBrW9IMGEGE9mmTed7TMKfqIrmLYyD7HCPX5YXxfpLyjv6I-_hyr0MrEdEqa5bULA'

DIRECTOR=
            'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkRGbEdBODQ5X0dsSjlJc0EycTQ4ciJ9.eyJpc3MiOiJodHRwczovL2dhdmluZ3VvLmF1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDE3MmJiYWU0MDQ5NTAwNmExNjE0NWYiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYxMzYwMTY1NywiZXhwIjoxNjEzNjg4MDU3LCJhenAiOiJlVTJwNnpVZWliTHF0Z2l6d0JncnFlZWhaaHN5SEozMSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9yIiwiZGVsZXRlOmFjdG9yIiwibW9kaWZ5OmFjdG9yIiwibW9kaWZ5Om1vdmllIiwidmlldzphY3RvcnMiLCJ2aWV3OmFzc2lnbiIsInZpZXc6bW92aWVzIl19.iNjw58sQoKtp6tB69Z-EJiNixol4dzUJ4BkXGgJ-wlK0KR4ImXfKygSnFcPCakt_i9cXS2VHlKmi3hU9VM6TchOgSLEjWOtajvbFGGuVCWveJj4eE3ixTVusOK90fXwywkdEmssglxstN8mZcBTTJ86aUorOTm8FGRmcXtRRYoNhyn7SCxD14xmkcmjma1JGgCLDHB93cOLwecSFC-_LAcAq_ewYOlcIbwV2ALw95vTVGVxgtY-PML4LtQujfKeNYUI3RRwKNKMreBqk_jkl2Z1oYTvsvQGEyvXeu6lfoZWAwSIX12XVV6uJ5RrXQCx8PBLDdwCWTOQnJZG3R7B8fA'

PRODUCER=
            'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkRGbEdBODQ5X0dsSjlJc0EycTQ4ciJ9.eyJpc3MiOiJodHRwczovL2dhdmluZ3VvLmF1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA0MDUwNjBjYWRiNzAwNjliMmYxNDkiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYxMzYwMTc4MywiZXhwIjoxNjEzNjg4MTgzLCJhenAiOiJlVTJwNnpVZWliTHF0Z2l6d0JncnFlZWhaaHN5SEozMSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9yIiwiYWRkOmFzc2lnbiIsImFkZDptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTphc3NpZ24iLCJkZWxldGU6bW92aWUiLCJtb2RpZnk6YWN0b3IiLCJtb2RpZnk6bW92aWUiLCJ2aWV3OmFjdG9ycyIsInZpZXc6YXNzaWduIiwidmlldzptb3ZpZXMiXX0.F9g8Qh4UUy4HDZJEyEMd-nPetzdtDbfoWYjrRaTFpo_3XjY4Iextez2sdDUfz-rK41V5tdd_R-gsbDE7tRVQNNlBLRxoCOZXEe6OKem-B0lir3VJ7HMvY-0vslE2v_7YyJPUENHiHb0Ug9L5RWkU0yDu06TrPhBgFreg6CSXu2KAYE8KRrDY9zVa6n84ldN89phjwq2BhQwrc9ow_G5DmJW6P9xckS9EHpCHLrYdiKsMWkE4uMpuJ4QxIjfL6-lYtzpNjOXcNrpPHfpfSOMniCFf58MYAac8I0hYkwv7LNgI5z5CkWFf3xHatRAzCwmscG-3FccJVEybvTxsYb7V4g'




## Endpoints

GET '/movies'
- Fetches all of movies
- Request Arguments: None
- Returns: movies, success
{
    "movies": [
        {
            "actors": [
                [
                    {
                        "actor_id": 1,
                        "actor_name": "Leonardo DiCaprio"
                    },
                    {
                        "actor_id": 2,
                        "actor_name": "Kate Winslet"
                    }
                ]
            ],
            "boxoffice": "2.195 billion USD",
            "id": 1,
            "release_date": "Sun, 12 Jan 1997 00:00:00 GMT",
            "title": "Titanic"
        },
        {
            "actors": [
                [
                    {
                        "actor_id": 1,
                        "actor_name": "Leonardo DiCaprio"
                    }
                ]
            ],
            "boxoffice": "836.8 million USD",
            "id": 2,
            "release_date": "Sun, 07 Feb 2010 00:00:00 GMT",
            "title": "Inception"
        }
    ],
    "success": true
}

POST '/movies/'
- Create a new movie
- Request Arguments: title,release_date,boxoffice
- Returns: movie,success
    {
            
        'success':  true,
        'movie':    {
                        "boxoffice": "2.195 billion USD",
                        "id": 1,
                        "release_date": "Sun, 12 Jan 1997 00:00:00 GMT",
                        "title": "Titanic"
                    }
    }

PATCH '/movies/<int:movie_id>'
- patch a movie
- Request Arguments: movie_id,title,release_date,boxoffice
- Returns: movie,success
    {
            
        'success':  true,
        'movie':    {
                        "boxoffice": "2.195 billion USD",
                        "id": 1,
                        "release_date": "Sun, 12 Jan 1997 00:00:00 GMT",
                        "title": "Titanic"
                    }
    }

DELETE '/movies/<int:movie_id>'
- Delete a movie
- Request Arguments: movie_id
- Returns: success,deleted movie id
{
    'success':true,
    "delete": movie_id 
}


GET '/actors'
- Fetches all of actors
- Request Arguments: None
- Returns: actors, success
{
    "actors": [
        {
            "age": "46",
            "gender": "Male",
            "id": 1,
            "movies": [
                [
                    {
                        "movie_id": 1,
                        "movie_name": "Titanic"
                    },
                    {
                        "movie_id": 2,
                        "movie_name": "Inception"
                    }
                ]
            ],
            "name": "Leonardo DiCaprio"
        },
        {
            "age": "45",
            "gender": "Female",
            "id": 2,
            "movies": [
                [
                    {
                        "movie_id": 1,
                        "movie_name": "Titanic"
                    }
                ]
            ],
            "name": "Kate Winslet"
        }
    ],
    "success": true

}

POST '/actors/'
- Create a new actor
- Request Arguments: name,age,gender
- Returns: actor,success
    {
            
        'success':  true,
        'actor':    {
                        "age": "45",
                        "gender": "Female",
                        "id": 2,
                        "name": "Kate Winslet"
                    }
    }

PATCH '/actors/<int:actor_id>'
- patch a actor
- Request Arguments: actor_id,name,age,gender
- Returns: actor,success
    {
            
        'success':  true,
        'actor':    {
                        "age": "45",
                        "gender": "Female",
                        "id": 2,
                        "name": "Kate Winslet"
                    }
    }

DELETE '/actors/<int:actor_id>'
- Delete a actor
- Request Arguments: actor_id
- Returns: success,deleted actor id
{
    'success':true,
    "delete": actor_id 
}

GET '/assigns'
- Fetches all of assigns
- Request Arguments: None
- Returns: assigns, success
{
   "assigns": [
        {
            "actor_id": 1,
            "id": 1,
            "movie_id": 1
        },
        {
            "actor_id": 2,
            "id": 2,
            "movie_id": 1
        },
        {
            "actor_id": 1,
            "id": 3,
            "movie_id": 2
        }
    ],
    "success": true

}

POST '/assigns/'
- Create a new assign
- Request Arguments: movie_id,actor_id
- Returns: assign,success
    {
            
        'success':  true,
        'assign':    {
                       "actor_id": 1,
                        "id": 3,
                        "movie_id": 2
                    }
    }

DELETE '/assigns/<int:assign_id>'
- Delete a assign
- Request Arguments: assign_id
- Returns: success,deleted assign id
{
    'success':true,
    "delete": assign_id 
}


### Roles:

- Casting Assistant
    Can view actors and movies

    Permissions: [
                    "view:actors",
                    "view:movies"
                ]

- Casting Director
    All permissions a Casting Assistant has and…
    Add or delete an actor from the database
    Modify actors or movies
    Can view assign

    Permissions: [
                        "add:actor",
                        "delete:actor",
                        "modify:actor",
                        "modify:movie",
                        "view:actors",
                        "view:assign",
                        "view:movies"
                    ]

- Executive Producer
    All permissions a Casting Director has and…
    Add or delete a movie from the database
    Assign actors to the movies
    Delete assign

    Permissions: [
                        "add:actor",
                        "add:assign",
                        "add:movie",
                        "delete:actor",
                        "delete:assign",
                        "delete:movie",
                        "modify:actor",
                        "modify:movie",
                        "view:actors",
                        "view:assign",
                        "view:movies"
                    ]



## Testing
To run the tests, run
```
python test_app.py
```