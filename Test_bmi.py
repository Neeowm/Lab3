import Lab2.bmi as bmi


def test_bmi_normal_weight():
    expectedresult=0
    testresult=bmi.calculate_bmi(1.6,50)
    assert (testresult==expectedresult)


def test_bmi_over_weight():
    expectedresult=1
    testresult=bmi.calculate_bmi(1.5,120)
    assert (testresult==expectedresult)


def test_bmi_under_weight():
    expectedresult=-1
    testresult=bmi.calculate_bmi(2.0,40)
    assert (testresult==expectedresult)