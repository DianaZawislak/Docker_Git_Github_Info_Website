"""This tests simple pages from project2"""



def test_request_aaatesting(client):
    """This tests AAA page"""
    response = client.get("/AAAtesting")
    assert response.status_code == 200
    assert b"What is AAA testing?" in response.data


def test_request_oop(client):
    """This tests OOP page"""
    response = client.get("/OOP")
    assert response.status_code == 200
    assert b"Local variables altered in the process are separate from local variab" in response.data


def test_request_pyliny(client):
    """This tests Pylint page"""
    response = client.get("/pyliny")
    assert response.status_code == 200
    assert b"What is Pytest?" in response.data


def test_request_solid(client):
    """This tests SOLID page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b"SOLIDbanner.png" in response.data

def test_request_page_not_found(client):
    """This tests page not found page"""
    response = client.get("/page5")
    assert response.status_code == 404
