import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import drop_db, setup_db, Book


class TestData():
    EXPECTED_EMPTY_DB_RESPONSE = {
        'success': True,
        'books': [],
        'total_books': 0
    }
    EXPECTED_ERROR_405_RESPONSE = {
        "success": False,
        "error": 405,
        "message": "Not allowed"
    }
    EXPECTED_CREATE_BOOK_RESPONSE = {
        'books': [{'author': 'Frank Wolf',
             'id': 1,
             'rating': 5,
             'title': 'genug haben'}],
        'created': 1,
        'success': True,
        'total_books': 1
    }
    EXPECTED_UPDATE_BOOK_RESPONSE = {
        'updated': 1,
        'success': True
    }
    EXPECTED_CREATE_TWO_BOOK_RESPONSE = {
        'books': [{'author': 'Frank Wolf',
             'id': 1,
             'rating': 5,
             'title': 'genug haben'},
             {'author': 'Frank Wolf',
                  'id': 2,
                  'rating': 4,
                  'title': 'Finanzen'}],
        'created': 2,
        'success': True,
        'total_books': 2
    }
    EXPECTED_ONE_BOOK_AFTER_DELETE = {
        'books': [{'author': 'Frank Wolf',
                  'id': 2,
                  'rating': 4,
                  'title': 'Finanzen'}],
        'deleted': 1,
        'success': True,
        'total_books': 1
    }
    EXPECTED_SEARCH_BOOK_RESULT = {
        "books": [
            {
            "author": "Frank Wolf",
            "id": 1,
            "rating": 5,
            "title": "genug haben"
            }
        ],
        "success": True,
        "total_books": 1
    }
    EXPECTED_SEARCH_BOOK_NO_RESULT = {
        "books": [],
        "success": True,
        "total_books": 0
    }




class BookshelfTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    # @classmethod
    # def setUpClass(cls):
    #     """Define test variables and initialize app."""
    #     cls.maxDiff=None
    #     cls.app = create_app()
    #     cls.client = cls.app.test_client
    #     cls.database_name = "bookshelf_test"
    #     cls.database_path = "postgresql://{}:{}@{}/{}".format('student', 'student', 'localhost:5432', cls.database_name)
    #     drop_db(cls.app, cls.database_path)

    # @classmethod
    # def tearDownClass(cls):
    #     """Define test variables and initialize app."""
    #     cls.maxDiff=None
    #     cls.app = create_app()
    #     cls.client = cls.app.test_client
    #     cls.database_name = "bookshelf_test"
    #     cls.database_path = "postgresql://{}:{}@{}/{}".format('student', 'student', 'localhost:5432', cls.database_name)
    #     drop_db(cls.app, cls.database_path)


    def setUp(self):
        """Define test variables and initialize app."""
        self.maxDiff=None
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "bookshelf_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format('student', 'student', 'localhost:5432', self.database_name)
        drop_db(self.app, self.database_path)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        Book.query.delete()

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_books_endpoint(self):
        """Test get books endpoint """
        res = self.client().get('/books')
        self.assertTrue(res)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), TestData.EXPECTED_EMPTY_DB_RESPONSE)

    def test_post_books_endpoint(self):
        """Test post to books endpoint """
        res = self.client().post('/books')
        self.assertEqual(res.status_code, 405)
        self.assertEqual(res.get_json(), TestData.EXPECTED_ERROR_405_RESPONSE)

    def test_error_405(self):
        """Test books endpoint """
        res = self.client().post('/books')
        self.assertEqual(res.status_code, 405)
        self.assertEqual(res.get_json(), TestData.EXPECTED_ERROR_405_RESPONSE)

    def test_post_book_endpoint(self):
        """Test create a book by post to book endpoint """
        res = self.client().post('/book', json={"title": "genug haben", "author": "Frank Wolf", "rating": 5})

        self.assertTrue(res)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), TestData.EXPECTED_CREATE_BOOK_RESPONSE)

    def test_patch_book_endpoint(self):
        """Test update a book by patch to book endpoint """
        res = self.client().post('/book', json={"title": "genug haben", "author": "Frank Wolf", "rating": 5})
        res = self.client().patch('/book/1', json={"rating": 3})

        data = json.loads(res.data)

        self.assertTrue(res)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), TestData.EXPECTED_UPDATE_BOOK_RESPONSE)


    def test_delete_book_endpoint(self):
        """Test remove a book by delete to book endpoint """
        res = self.client().post('/book', json={"title": "genug haben", "author": "Frank Wolf", "rating": 5})
        res = self.client().post('/book', json={"title": "Finanzen", "author": "Frank Wolf", "rating": 4})

        self.assertTrue(res)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), TestData.EXPECTED_CREATE_TWO_BOOK_RESPONSE)

        res = self.client().delete('/book/1', json={"rating": 3})

        self.assertTrue(res)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), TestData.EXPECTED_ONE_BOOK_AFTER_DELETE)


    def test_search_book_endpoint(self):
        """Test find a book by usin gsearch endpoint """
        book = Book(
            title='genug haben',
            author='Frank Wolf',
            rating=5
        )
        book.insert()

        res = self.client().get('/books/search?q=genug')
        r = res.get_json()

        expected_title = 'genug haben'
        result_title = r['books'][0]['title']

        self.assertTrue(res)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(result_title, expected_title)
        self.assertEqual(r, TestData.EXPECTED_SEARCH_BOOK_RESULT)

    def test_invalid_search_book_endpoint(self):
        """Test find a book by usin gsearch endpoint """
        book = Book(
            title='genug haben',
            author='Frank Wolf',
            rating=5
        )
        book.insert()

        res = self.client().get('/books/search?q=Quality')
        r = res.get_json()


        self.assertTrue(res)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(r, TestData.EXPECTED_SEARCH_BOOK_NO_RESULT)



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
