from basic3 import carre


def test_carre():
    resCarre=carre(4)
    assert resCarre == 16
    #logger.info("carre(4)=" + str(resCarre))

# nb: lancement du test via la commande:
#     pytest test_basic3.py   
