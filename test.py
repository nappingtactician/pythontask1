import main
from main import app
import unittest


class TestMain(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/v1/sanitized")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_content(self):
        tester = app.test_client(self)
        response = tester.get("/v1/sanitized")
        self.assertEqual(response.content_type, "application/json")

    def test_response_return(self):
        tester = app.test_client(self)
        response = tester.get("/v1/sanitized")
        self.assertTrue(b'result' in response.data)


if __name__ == "__main__":
    unittest.main()
