from instruments import Spectrometer

def test_init():
    # tests that the spectrometer is initialized with the correct name and starts as off
    s = Spectrometer('Name')
    assert s.name == 'Name'
    assert s.is_on is False
    


def test_power():
    # tests to make sure the power switch function turns the spectrometer on
    s = Spectrometer('Name')
    s.power_switch()
    assert s.is_on is True



def test_measurement():
    # tests to make sure the spectrometer can take a reading when its turned on and cant when its turned off
    s = Spectrometer('Name')
    before = s.take_reading(500)
    s.power_switch()
    after = s.take_reading(500)
    assert before is False and after is True