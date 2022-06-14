import ipdb

class TestAuth:

    def test_should_access_home(self, client):
        #ipdb.set_trace()
        assert client.get('/').status_code == 200

    def test_should_redirect_known_email(self, client):
        email = "john@simplylift.co"
        response = client.post('/showSummary', data={'email' : email})
        assert response.status_code == 200

    def test_unknown_email_should_return_error(self, client):
        email = 'adress@test.fr'
        response = client.post('/showSummary', data={'email' : email})
        assert response.status_code == 302