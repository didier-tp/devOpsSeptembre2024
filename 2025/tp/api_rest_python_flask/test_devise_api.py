from devise_api import app

# Import pytest for writing and running tests
import pytest

@pytest.fixture
def client():
    """A test client for the app."""
    with app.test_client() as client:
        yield client

def test_get_carre(client):
    response = client.get('/devise-api/v1/calculs/carre/9')
    assert response.status_code == 200
    assert response.json == {"x":9 , "carre": 81}
    print(f"carre(9)=>response.json={response.json}")
    
def test_get_racine_carree(client):
    response = client.get('/devise-api/v1/calculs/racine_carree/9')
    assert response.status_code == 200
    assert response.json == {"x":9 , "racine": 3}
    print(f"racine_carree(9)=>response.json={response.json}")

# nb: lancement du test via la commande:
#     pytest -s test_devise_api.py   
# ---------
# sous windows ou autre , installation de pytest via 
#     pip install pytest
