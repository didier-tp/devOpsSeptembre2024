from basic import addition
#import logging

#logging.basicConfig(level=logging.DEBUG)
#logger = logging.getLogger()

def test_addition():
    resAdd=addition(3,5)
    assert resAdd == 8
    #logger.info("addition(3,5)=" + str(resAdd))

# nb: lancement du test via la commande:
#     pytest test_basic.py   
# ---------
# sous windows ou autre , installation de pytest via 
#     pip install pytest
#-----------
# sous python3 et debian , installation de pytest via
#     sudo apt install python3-pytest 