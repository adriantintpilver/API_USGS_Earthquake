import unittest
import requests

class TestAPI(unittest.TestCase):
    def test_search(self, url, expected_result):
        response = requests.get(url)
        self.assertEqual(response.status_code, 200, f"Test failed: The API returned a {response.status_code} status code.")
        self.assertTrue(response.text.strip() == expected_result.strip(), f"Test failed: The API response did not match the expected result. Expected result: {expected_result.strip()}. Actual result: {response.text.strip()}")
        return response.text

if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/search?city=Buenos%20Aires&start_date=2004-04-02&end_date=2018-01-31'
    expected_result = '{"message":"Result for Buenos Aires between 2004-04-02 and 2018-01-31: The closest earthquake was a M 5.5 - 27 km WSW of Atiquipa, Peru on January 30 2018"}'
    try:
        result = TestAPI().test_search(url, expected_result)
        print("Test succeeded: The API response matched the expected result.")
    except AssertionError as e:
        print(str(e))