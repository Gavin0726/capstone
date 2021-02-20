import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Assign, Movie, Actor


class CapstoneTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = 'postgresql://gavin@localhost:5432/capstone_test'
        setup_db(self.app, self.database_path)

        self.Assistant_jwt = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkRGbEdBODQ5X0dsSjlJc0EycTQ4ciJ9.eyJpc3MiOiJodHRwczovL2dhdmluZ3VvLmF1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDJiMTU4YmRlNTViYzAwNmZjMzc1ZTciLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYxMzYwMjIzMiwiZXhwIjoxNjEzNjg4NjMyLCJhenAiOiJlVTJwNnpVZWliTHF0Z2l6d0JncnFlZWhaaHN5SEozMSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsidmlldzphY3RvcnMiLCJ2aWV3Om1vdmllcyJdfQ.A46JefmyOYXRVpyQGCHMS37xBnN3WQXpboBA47Q9Hriv0HQFYgzvKOhc1L3Obirw9rqxRXEiJ7hibddFxbekcUabCvibUJBKnUxNMAI6N-V3eGFFcIHg1DmrGL0xmcdptlELruK_vW4xIl7w_g9jhbksluR4Gb96rDTLPgz4DqdGleEHsATCxEIIOZPsZQLTHxzolHWouDqz65tJIcgGVwEOuRgkLWgc7XrT1vzRoHb6AknBpCcdctqUdyyUICf8RbySoJWWNaH3bocF7i9yOCBrW9IMGEGE9mmTed7TMKfqIrmLYyD7HCPX5YXxfpLyjv6I-_hyr0MrEdEqa5bULA'
                    }
        self.Director_jwt = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkRGbEdBODQ5X0dsSjlJc0EycTQ4ciJ9.eyJpc3MiOiJodHRwczovL2dhdmluZ3VvLmF1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDE3MmJiYWU0MDQ5NTAwNmExNjE0NWYiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYxMzYwMTY1NywiZXhwIjoxNjEzNjg4MDU3LCJhenAiOiJlVTJwNnpVZWliTHF0Z2l6d0JncnFlZWhaaHN5SEozMSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9yIiwiZGVsZXRlOmFjdG9yIiwibW9kaWZ5OmFjdG9yIiwibW9kaWZ5Om1vdmllIiwidmlldzphY3RvcnMiLCJ2aWV3OmFzc2lnbiIsInZpZXc6bW92aWVzIl19.iNjw58sQoKtp6tB69Z-EJiNixol4dzUJ4BkXGgJ-wlK0KR4ImXfKygSnFcPCakt_i9cXS2VHlKmi3hU9VM6TchOgSLEjWOtajvbFGGuVCWveJj4eE3ixTVusOK90fXwywkdEmssglxstN8mZcBTTJ86aUorOTm8FGRmcXtRRYoNhyn7SCxD14xmkcmjma1JGgCLDHB93cOLwecSFC-_LAcAq_ewYOlcIbwV2ALw95vTVGVxgtY-PML4LtQujfKeNYUI3RRwKNKMreBqk_jkl2Z1oYTvsvQGEyvXeu6lfoZWAwSIX12XVV6uJ5RrXQCx8PBLDdwCWTOQnJZG3R7B8fA'
                    }
        self.Producer_jwt = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkRGbEdBODQ5X0dsSjlJc0EycTQ4ciJ9.eyJpc3MiOiJodHRwczovL2dhdmluZ3VvLmF1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA0MDUwNjBjYWRiNzAwNjliMmYxNDkiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYxMzYwMTc4MywiZXhwIjoxNjEzNjg4MTgzLCJhenAiOiJlVTJwNnpVZWliTHF0Z2l6d0JncnFlZWhaaHN5SEozMSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9yIiwiYWRkOmFzc2lnbiIsImFkZDptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTphc3NpZ24iLCJkZWxldGU6bW92aWUiLCJtb2RpZnk6YWN0b3IiLCJtb2RpZnk6bW92aWUiLCJ2aWV3OmFjdG9ycyIsInZpZXc6YXNzaWduIiwidmlldzptb3ZpZXMiXX0.F9g8Qh4UUy4HDZJEyEMd-nPetzdtDbfoWYjrRaTFpo_3XjY4Iextez2sdDUfz-rK41V5tdd_R-gsbDE7tRVQNNlBLRxoCOZXEe6OKem-B0lir3VJ7HMvY-0vslE2v_7YyJPUENHiHb0Ug9L5RWkU0yDu06TrPhBgFreg6CSXu2KAYE8KRrDY9zVa6n84ldN89phjwq2BhQwrc9ow_G5DmJW6P9xckS9EHpCHLrYdiKsMWkE4uMpuJ4QxIjfL6-lYtzpNjOXcNrpPHfpfSOMniCFf58MYAac8I0hYkwv7LNgI5z5CkWFf3xHatRAzCwmscG-3FccJVEybvTxsYb7V4g'
                    }
        self.Producer_jwt_token_expired = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkRGbEdBODQ5X0dsSjlJc0EycTQ4ciJ9.eyJpc3MiOiJodHRwczovL2dhdmluZ3VvLmF1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA0MDUwNjBjYWRiNzAwNjliMmYxNDkiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYxMzUxMDI0MiwiZXhwIjoxNjEzNTk2NjQyLCJhenAiOiJlVTJwNnpVZWliTHF0Z2l6d0JncnFlZWhaaHN5SEozMSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9yICIsImFkZDphc3NpZ24iLCJhZGQ6bW92aWUiLCJkZWxldGU6YWN0b3IiLCJkZWxldGU6YXNzaWduIiwiZGVsZXRlOm1vdmllIiwibW9kaWZ5OmFjdG9yIiwibW9kaWZ5Om1vdmllIiwidmlldzphY3RvcnMiLCJ2aWV3OmFzc2lnbiIsInZpZXc6bW92aWVzIl19.h8-SSZHvVFjlhhBl5I6Qdj463wdsSpFMRKKeprsonqyW9Pn_aBIP7fIYDHksRGtceQkdklluKCFGu2SmlkcgcEZ5k0J9TrKjFcAByHXWbCrbe5TezPuo68cSmlcewNy3Fnn9aQa0IblrWwv64XKGr1iwBE3TDa5IWeuDQwxq9DTMIwRCO8FAHcy_ysYIPOylw4k748E9GTEmzhsNvixI-eNCleaOh7rgfQunrz9VjaW1lanOLJLEWda0LgRsgrpebC5y2PDHpfzmCUX1b67d1ghSKsmko9mQgnMcVp2oi-CNtWUq9S2YXkmLWj2VMPpKM6vOHExHCfCG0rMf4NERAw'
                    }
        self.new_movie = {
            'title': 'Titanic',
            'release_date': '1/12/1997',
            'boxoffice': '2.195 billion USD'
        }
        self.patch_movie = {
            'title': 'Inception',
            'release_date': '2/07/2010',
            'boxoffice': "836.8 million USD"
        }

        self.new_actor = {
            'title': 'Leonardo DiCaprio',
            'age': '46',
            'gender': "Male"
        }
        self.patch_actor = {
            'title': 'Kate Winslet',
            'age': '45',
            'gender': "Female"
        }

        self.new_assign = {
            'movie_id': '1',
            'actor_id': '1'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    '''
    test movies
    '''

    def test_00_create_new_movie(self):
        res = self.client().post(
                                    '/movies',
                                    json=self.new_movie,
                                    headers=self.Producer_jwt
                                )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['movie'])

    def test_01_get_movies(self):
        res = self.client().get('/movies', headers=self.Assistant_jwt)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['movies'])

    def test_02_patch_movie(self):
        res = self.client().patch(
                                    '/movies/1',
                                    json=self.patch_movie,
                                    headers=self.Producer_jwt
                                )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['movie'])

    def test_03_403_if_movie_creation_unauthorized(self):
        res = self.client().post(
                                '/movies',
                                json=self.new_movie,
                                headers=self.Director_jwt
                                )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unauthorized')

    def test_04_405_if_movie_creation_not_allowed(self):
        res = self.client().post(
                                '/movies/1',
                                json=self.new_movie,
                                headers=self.Producer_jwt
                                )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_05_401_if_movie_patch_token_expired(self):
        res = self.client().patch(
                                '/movies/1',
                                json=self.patch_movie,
                                headers=self.Producer_jwt_token_expired
                                )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'token_expired')

    def test_06_400_if_movie_does_not_exist(self):
        res = self.client().delete('/movies/1000', headers=self.Producer_jwt)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

        
    '''
    test actors
    '''
    def test_07_create_new_actor(self):
        res = self.client().post(
                                    '/actors',
                                    json=self.new_actor,
                                    headers=self.Director_jwt
                                )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['actor'])

    def test_08_get_actors(self):
        res = self.client().get('/actors', headers=self.Assistant_jwt)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['actors'])

    def test_09_patch_actor(self):
        res = self.client().patch(
                                    '/actors/1',
                                    json=self.patch_actor,
                                    headers=self.Director_jwt
                                )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['actor'])

    def test_10_403_if_actor_creation_unauthorized(self):
        res = self.client().post(
                                '/actors',
                                json=self.new_actor,
                                headers=self.Assistant_jwt
                                )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unauthorized')

    def test_11_405_if_actor_creation_not_allowed(self):
        res = self.client().post(
                                '/actors/1',
                                json=self.new_actor,
                                headers=self.Director_jwt
                                )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_12_403_if_actor_patch_unauthorized(self):
        res = self.client().patch(
                                '/actors/1',
                                json=self.patch_actor,
                                headers=self.Assistant_jwt
                                )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unauthorized')

    def test_13_400_if_actor_does_not_exist(self):
        res = self.client().delete('/actors/1000', headers=self.Director_jwt)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    '''
    test assigns
    '''

    def test_14_create_new_assign(self):
        res = self.client().post(
                                    '/assigns',
                                    json=self.new_assign,
                                    headers=self.Producer_jwt
                                )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['assign'])

    def test_15_get_assigns(self):
        res = self.client().get('/assigns', headers=self.Producer_jwt)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['assigns'])

    def test_16_403_if_assign_creation_unauthorized(self):
        res = self.client().post(
                                '/assigns',
                                json=self.new_assign,
                                headers=self.Director_jwt
                                )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unauthorized')

    def test_17_405_if_assign_creation_not_allowed(self):
        res = self.client().post(
                                '/assigns/1',
                                json=self.new_assign,
                                headers=self.Producer_jwt
                                )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_18_400_if_assign_does_not_exist(self):
        res = self.client().delete('/assigns/1000', headers=self.Producer_jwt)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    '''
    test delete assign, actor, movie
    '''
    def test_19_delete_assign(self):
        res = self.client().delete('/assigns/1', headers=self.Producer_jwt)
        data = json.loads(res.data)
        assign = Assign.query.filter(Assign.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 1)
        self.assertEqual(assign, None)

    def test_20_delete_movie(self):
        res = self.client().delete('/movies/1', headers=self.Producer_jwt)
        data = json.loads(res.data)
        movie = Movie.query.filter(Movie.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 1)
        self.assertEqual(movie, None)

    def test_21_delete_actor(self):
        res = self.client().delete('/actors/1', headers=self.Director_jwt)
        data = json.loads(res.data)
        actor = Actor.query.filter(Actor.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 1)
        self.assertEqual(actor, None)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
