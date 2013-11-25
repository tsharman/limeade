import unittest
import mock
import tornado.testing
import limeade.app


class IntegTest(tornado.testing.AsyncHTTPTestCase):

    def get_app(self):
        return limeade.app.App()

    def test_homepage(self):
        response = self.fetch('/')
        assert response.code is 200
        response = self.fetch('/videos/?filter=new')
        assert response.code is 200
        response = self.fetch('/videos/?filter=trending')
        assert response.code is 200
        
