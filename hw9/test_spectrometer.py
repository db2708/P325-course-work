from instruments import Spectrometer

def test_init():
    spec = Spectrometer("Spec_test")
    assert spec.name == "Spec_test"
    assert spec.is_on is True
    


# def test_power():
#     pass

# def test_measurement():
#     pass