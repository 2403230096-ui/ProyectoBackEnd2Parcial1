from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class PartidasAPITests(APITestCase):
    def setUp(self):
        self.u1 = User.objects.create_user('test', password='pass1234')
        self.u2 = User.objects.create_user('otro', password='pass1234')

    def _token(self, username):
        r = self.client.post('/api/login/', {'username': username, 'password': 'pass1234'})
        self.assertEqual(r.status_code, 200)
        return r.data['token']

    def test_sin_token_es_401(self):
        self.assertEqual(self.client.get('/api/partidas/').status_code, 401)

    def test_login_incorrecto_es_400(self):
        r = self.client.post('/api/login/', {'username': 'test', 'password': 'mal'})
        self.assertEqual(r.status_code, 400)

    def test_crear_y_listar_solo_las_propias(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self._token('test'))
        r = self.client.post('/api/partidas/', {'nombre': 'Run 1', 'juego': 'oot'})
        self.assertEqual(r.status_code, 201)
        self.assertEqual(len(self.client.get('/api/partidas/').data), 1)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self._token('otro'))
        self.assertEqual(len(self.client.get('/api/partidas/').data), 0)

    def test_cors_permite_vite(self):
        r = self.client.options(
            '/api/partidas/',
            HTTP_ORIGIN='http://localhost:5173',
            HTTP_ACCESS_CONTROL_REQUEST_METHOD='POST',
        )
        self.assertEqual(r['Access-Control-Allow-Origin'], 'http://localhost:5173')
