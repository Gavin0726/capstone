import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Assign, Movie, Actor


class CapstoneTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = 'postgresql://gavin@localhost:5432/capstone_test'
        setup_db(self.app, self.database_path)
        self.Assistant_jwt = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkRGbEdBODQ5X0dsSjlJc0EycTQ4ciJ9.eyJpc3MiOiJodHRwczovL2dhdmluZ3VvLmF1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDE3MmJiYWU0MDQ5NTAwNmExNjE0NWYiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYxMzM1MDIwMiwiZXhwIjoxNjEzMzU3NDAyLCJhenAiOiJlVTJwNnpVZWliTHF0Z2l6d0JncnFlZWhaaHN5SEozMSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9yICIsImRlbGV0ZTphY3RvciIsIm1vZGlmeTphY3RvciIsIm1vZGlmeTptb3ZpZSIsInZpZXc6YWN0b3JzIiwidmlldzphc3NpZ24iLCJ2aWV3Om1vdmllcyJdfQ.xQ71lZKTNymhdjRKKwxC-wLMaIsnyterMc6GbK87ngE0Onl4WBv9IawQJ8vEuPKKkMW6u_3F9vkUXvo_dNsgCVx1xbCDQv8EWGIgFcZomlhOJaLiLfMsztkTslolvnJERfRN5Cdr6iiL8Q7cw8oLUGHEBVn6HIy-uWs_A7UbKRFZhmZNxcPaMlyMgrSercYOin99O3jiQbtacT8x4os_7Cj4FfEVEkdp-3u6K2v0jEIX_6f5-17C6bpRBPzdKPXhtasq2GKkKN7O2N0FT3Gyfvu3xWsU7mzj17oTPd2pgbIgLE-9kdJhyepb67z5VnnmYtNoTGXi3toGC2COOPQXGg'
                    }

        self.new_movie = {
            'title': 'Titanic',
            'release_date': '17/12/1997',
            'boxoffice': "2.195 billion USD"
        }
        # self.new_movie2 = {
        #     'title': 'Inception',
        #     'release_date': '22/07/2010',
        #     'boxoffice': "836.8 million USD"
        # }

        self.new_actor = {
            'title': 'Leonardo DiCaprio',
            'age': '46',
            'gender': "Male"
        }
        # self.new_actor2 = {
        #     'title': 'Kate Winslet',
        #     'age': '45',
        #     'gender': "Female"
        # }

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

    def test_get_movies(self):
        res = self.client().get('/movies', headers=self.Assistant_jwt)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # self.assertIsNotNone(data['movies'])

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation
    and for expected errors.

    """
    # def test_get_paginated_questions(self):
    #     res = self.client().get('/questions')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['current_category'], 1)
    #     self.assertEqual(data['total_questions'], 18)

    # def test_404_sent_requesting_beyond_valid_page(self):
    #     res = self.client().get('/questions?page=1000')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'resource not found')

    # def test_get_question_search_with_results(self):
    #     res = self.client().post('/questions', json={'searchTerm': 'Africa'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(len(data['questions']), 1)

    # def test_get_question_search_without_results(self):
    #     res = self.client().post('/questions', json={'searchTerm': 'USA'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(len(data['questions']), 0)

    def test_create_new_actor(self):
        res = self.client().post('/actors', json=self.new_actor, headers=self.Assistant_jwt)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # def test_405_if_book_creation_not_allowed(self):
    #     res = self.client().post('/questions/45', json=self.new_question)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 405)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'method not allowed')

    # def test_delete_question(self):
    #     res = self.client().delete('/questions/5')
    #     data = json.loads(res.data)
    #     question = Question.query.filter(Question.id == 5).one_or_none()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['deletedid'], 5)
    #     self.assertEqual(question, None)

    # def test_400_if_question_does_not_exist(self):
    #     res = self.client().delete('/questions/1000')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 400)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'bad request')

    # def test_given_behavior(self):
    #     """Test _____________ """
    #     res = self.client().get('/')

    #     self.assertEqual(res.status_code, 200)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()

