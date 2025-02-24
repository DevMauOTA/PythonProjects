from BandNameGenerator import Bandname_Generator


def test_outputWelcometest(capsys):
    band_name_generator = Bandname_Generator()
    band_name_generator.start()

    captured = capsys.readouterr()
    assert captured.out == "Welcome to the Band Name Generator.\n"


def test_inputWithQuestionText(capsys):
    band_name_generator = Bandname_Generator()
    band_name_generator.start()

    captured = capsys.readouterr()
    assert captured.out == "What's the name of the city ou grew in?\n"
