import pytest
from bandnamegenerator import BandNameGenerator


@pytest.fixture()
def beforeAll():
    init_program = BandNameGenerator()
    init_program.run()


def test_initProgram():
    init_program = BandNameGenerator()
    init_program.run()


def test_welcome_text_is_show(capfd):
    init_program = BandNameGenerator()
    init_program.run()

    out, err = capfd.readouterr()

    assert out == "Welcome to the Band Name Generator.\n"
