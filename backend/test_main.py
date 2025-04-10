from fastapi.testclient import TestClient

from main import app


client = TestClient(app)
    
def test_teach_grades():
    response = client.get("api/teach/grades")
    assert response.status_code == 200
    # data = response.json()
    # assert isinstance(data, list)



