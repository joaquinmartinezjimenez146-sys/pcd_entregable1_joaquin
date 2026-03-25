import pytest
from flota import CazaEstelar, Repuesto, StockInsuficienteError

def test_instanciacion_caza():
    caza = CazaEstelar("TIE Interceptor", ["Láser doble"], 1, "TIE-INT", 777)
    assert caza.nombre == "TIE Interceptor"
    assert caza.catalogo_repuestos == ["Láser doble"]
    assert caza. id_combate == "TIE-INT"

def test_extraccion_repuesto_exito():
    motor = Repuesto("Motor Iónico", "Proveedor A", 10, 5000)
    assert motor.extraer_repuesto(4) 
    assert motor.cantidad == 6

def test_extrraccion_repuesto_excepcion():
    motor = Repuesto("Motor Iónico", "Proveedor A", 2, 5000)
    with pytest.raises(StockInsuficienteError):
        motor.extraer_repuesto(5)