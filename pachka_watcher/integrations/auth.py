from httpx import Auth


class PachkaAuth(Auth):
    def __init__(self, token):
        self.token = token

    def auth_flow(self, request):
        request.headers['Authorization'] = 'Bearer {}'.format(self.token)
        yield request
