from basic2 import multiplication

def test_multiplication():
    resMult=multiplication(3,5)
    print("multiplication(3,5)=" + str(resMult))
    assert resMult == 15
   
# nb: lancement du test via la commande:
#     pytest test_basic2.py   
