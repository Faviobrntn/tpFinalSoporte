import unittest
from DBase import Tablas
from Negocio import ABMShow


class showTest(unittest.TestCase):
    #valida que el show no exista en la bd
    def test_validarShow(self):
        #Lord, All Men Can't Be Dogs id pelicula=71466
        #La casa de papel id serie=71466 (ya se encuentra en la BD)
        abm=ABMShow.ABMShow()
        pelicula=Tablas.Show()
        pelicula.tipo=0 #(pelicula)
        pelicula.idShow=71466
        self.assertTrue(abm.validarShow(pelicula))
        se=Tablas.Show()
        se.idShow=71466
        se.tipo=1
        self.assertFalse(abm.validarShow(se))
        #tiene que dar False, porque ya existe en la base de datos
        #lo raro es que cuando vuelvo a agregar la serie, no la agrega.. o sea que si ejecuta el metodo y ahi anda bien (aca no)


if __name__ == '__main__':
    unittest.main()
