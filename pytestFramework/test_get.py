import requests
import json
import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_useValidParam(self, dataBaseUrl, parms, responseDataGet):
        validBaseURL, _ = dataBaseUrl
        userId, id, _, _ = parms
        url = f"{validBaseURL}{userId}{id}"
        print("GET URL: " + url)
        response = requests.get(url)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=1)
        print("json response body:", json_str)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        print(f"Response Status Code: {response.status_code}")
        expectedGetUserId, expectedGetId, expectedGetTitle, expectedGetBody = responseDataGet
        assert isinstance(json_data, list), f"Expected list, but got {type(json_data)}"
        first_item = json_data[0]

        assert first_item["userId"] == int(expectedGetUserId), f"Expected userId {expectedGetUserId}, but got {first_item.get('userId')}"
        assert first_item["id"] == int(expectedGetId), f"Expected id {expectedGetId}, but got {first_item.get('id')}"
        assert first_item["title"] == expectedGetTitle, f"Expected title '{expectedGetTitle}', but got '{first_item.get('title')}'"
        assert first_item["body"] == expectedGetBody, f"Expected body '{expectedGetBody}', but got '{first_item.get('body')}'"

    def test_OnlyUseTitleParam (self, dataBaseUrl, parms, responseDataGet):
        validBaseURL, _ = dataBaseUrl
        _, _, title, _ = parms
        url = f"{validBaseURL}{title}"
        print("GET URL: " + url)
        response = requests.get(url)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=1)
        print("json response body:", json_str)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        print(f"Response Status Code: {response.status_code}")
        _, _, expectedGetTitle, _ = responseDataGet
        assert isinstance(json_data, list), f"Expected list, but got {type(json_data)}"
        first_item = json_data[0]
        assert first_item["title"] == expectedGetTitle, f"Expected title '{expectedGetTitle}', but got '{first_item.get('title')}'"

    def test_OnluUse(self, dataBaseUrl, parms, responseDataGet):
        validBaseURL, _ = dataBaseUrl
        _, _, _, onlyID = parms
        url = f"{validBaseURL}{onlyID}"
        print("GET URL: " + url)
        response = requests.get(url)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=1)
        print("json response body:", json_str)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        print(f"Response Status Code: {response.status_code}")
        expectedGetUserId, expectedGetId, expectedGetTitle, expectedGetBody = responseDataGet
        assert isinstance(json_data, list), f"Expected list, but got {type(json_data)}"
        first_item = json_data[0]
        assert first_item["userId"] == int(expectedGetUserId), f"Expected userId {expectedGetUserId}, but got {first_item.get('userId')}"
        assert first_item["id"] == int(expectedGetId), f"Expected id {expectedGetId}, but got {first_item.get('id')}"
        assert first_item["title"] == expectedGetTitle, f"Expected title '{expectedGetTitle}', but got '{first_item.get('title')}'"
        assert first_item["body"] == expectedGetBody, f"Expected body '{expectedGetBody}', but got '{first_item.get('body')}'"

    def test_invalidGetUrl (self, dataBaseUrl, parms):
        _, invalidBasedURL = dataBaseUrl
        userId, id, _, _ = parms
        url = f"{invalidBasedURL}{userId}{id}"
        print("GET URL: " + url)
        response = requests.get(url)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=1)
        print("json response body:", json_str)
        assert response.status_code == 404, f"Expected status code 200, but got {response.status_code}"
        print(f"Response Status Code: {response.status_code}")

    def test_invalidUserId (setup, dataBaseUrl, invalidParms):
        validBaseURL, _ = dataBaseUrl
        invalidUserId, _, _ = invalidParms
        url = f"{validBaseURL}{invalidUserId}"
        print("GET URL: " + url)
        response = requests.get(url)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=1)
        print("json response body:", json_str)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        print(f"Response Status Code: {response.status_code}")
        assert response.text == "[]", "Expected response body to be blank, but it was not."
        print("Response body is blank as expected.")

    def test_invalidId(setup, dataBaseUrl, invalidParms):
        validBaseURL, _ = dataBaseUrl
        _, invalid, _ = invalidParms
        url = f"{validBaseURL}{invalid}"
        print("GET URL: " + url)
        response = requests.get(url)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=1)
        print("json response body:", json_str)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        print(f"Response Status Code: {response.status_code}")
        assert response.text == "[]", "Expected response body to be blank, but it was not."
        print("Response body is blank as expected.")

    def test_invalidTitle(setup, dataBaseUrl, invalidParms):
        validBaseURL, _ = dataBaseUrl
        _, _, invalidTitle = invalidParms
        url = f"{validBaseURL}{invalidTitle}"
        print("GET URL: " + url)
        response = requests.get(url)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=1)
        print("json response body:", json_str)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        print(f"Response Status Code: {response.status_code}")
        assert response.text == "[]", "Expected response body to be blank, but it was not."
        print("Response body is blank as expected.")
        










