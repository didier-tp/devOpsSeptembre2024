from basic2 import multiplication


def test_multiplication():
    resMult=multiplication(3,5)
    assert resMult == 15
    #logger.info("addition(3,5)=" + str(resMult))

# nb: lancement du test via la commande:
#     pytest test_basic2.py   
