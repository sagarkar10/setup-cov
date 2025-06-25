from services.service1.src.main import super_calc

def test_super_calc():
    assert super_calc(2,1) == 2

def test_super_calc_fail():
    assert super_calc(1,2) == 2


