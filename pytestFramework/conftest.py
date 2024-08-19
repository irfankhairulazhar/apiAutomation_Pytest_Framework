import pytest

#global setup
@pytest.fixture(scope="class")
def setup():
    try:
        print("Setup complete")
        # Example setup code, e.g., initialize resources
        yield
    except Exception as e:
        print(f"Setup failed: {e}")
        raise
    finally:
        # Teardown code
        print("Teardown complete")

#basedPostURL
@pytest.fixture()
def dataBaseUrl ():
     validBaseURL = "https://jsonplaceholder.typicode.com/posts"
     invalidBasedURL = "https://jsonplaceholder.typicode.com/postss"
     return validBaseURL, invalidBasedURL

#baseJsonData
@pytest.fixture()
def jsonData ():
    data = {
        "userId": 4,
        "title": "lalalalal",
        "body": "hihihi"
    }
    return data

#verifyDataResponse
@pytest.fixture()
def jsonDataResponse ():
    expectedPostuserId = 4
    expectedPostTitle = "lalalalal"
    expectedBody = "hihihi"
    return expectedPostuserId, expectedPostTitle, expectedBody


@pytest.fixture()
def parms ():
    userId = "?userId=2&"
    id = "id=12"
    title = "?title=in quibusdam tempore odit est dolorem"
    onlyID ="?id=12"
    return userId, id, title, onlyID

@pytest.fixture()
def responseDataGet ():
    expectedGetUserId = 2
    expectedGetId = 12
    expectedGetTitle = "in quibusdam tempore odit est dolorem"
    expectedGetBody = "itaque id aut magnam\npraesentium quia et ea odit et ea voluptas et\nsapiente quia nihil amet occaecati quia id voluptatem\nincidunt ea est distinctio odio"
    return expectedGetUserId, expectedGetId, expectedGetTitle, expectedGetBody

@pytest.fixture()
def invalidParms ():
    invalidUserId = "?userId=200"
    invalid = "?id=200"
    invalidTitle = "?title=in quibusdam tempore odit est doloremll"
    return invalidUserId, invalid, invalidTitle

