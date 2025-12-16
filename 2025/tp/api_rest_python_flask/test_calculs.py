from calculs import carre,racine_carree

def test_carre():
    res=carre(3)
    assert res==9
    print(f"carre(3)={res}")
    
def test_racine_carree():
    res=racine_carree(25)
    assert res==5
    print(f"racine_carree(25)={res}")    

# nb: lancement du test via la commande:
#     pytest -s test_calculs.py   
# ---------
# sous windows ou autre , installation de pytest via 
#     pip install pytest
