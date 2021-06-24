import main
from main import app
import unittest
import pandas as pd


class TestMain(unittest.TestCase):
    # def test_index(self):
    #     tester = app.test_client(self)
    #     response = tester.get("/v1/sanitized")
    #     statuscode = response.status_code
    #     self.assertEqual(statuscode, 200)
    #
    # def test_content(self):
    #     tester = app.test_client(self)
    #     response = tester.get("/v1/sanitized")
    #     self.assertEqual(response.content_type, "application/json")

    def test_case(self):
        passcount = 0
        failcount = 0
        data = pd.read_excel('test case.xlsx')
        with app.test_request_context():
            for i in range(8):
                ans = main.testing(data['username'][i], data['password'][i])
                if ans['result'] == data['result'][i]:
                    passcount += 1
                else:
                    failcount += 1
            if passcount == 8:
                pass


if __name__ == "__main__":
    unittest.main()
