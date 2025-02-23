from BandNameGenerator import Bandname_Generator


def test_outPut(capsys):
    band_name_generator = Bandname_Generator()
    band_name_generator.start()

    captured = capsys.readouterr()
    assert captured.out == "Bandname generator\n"
