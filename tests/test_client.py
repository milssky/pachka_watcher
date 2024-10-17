from pachka_watcher.integrations.auth import PachkaAuth


class TestPachkaAuth:

    def test_init(self):
        auth = PachkaAuth('test_token')
        assert auth.token == 'test_token'
