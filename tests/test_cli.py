from toolkit.__main__ import main


def test_cli_calc_success(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.argv",
        ["toolkit", "calc", "2+3*4"],
    )

    result = main()

    captured = capsys.readouterr()

    assert result == 0
    assert captured.out.strip() == "14"

def test_cli_calc_error(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.argv",
        ["toolkit", "calc", "1/0"],
    )

    result = main()

    captured = capsys.readouterr()

    assert result == 2
    assert "Calculator error" in captured.err

def test_cli_convert_success(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.argv",
        [
            "toolkit",
            "convert",
            "1000",
            "--from",
            "mm",
            "--to",
            "m",
        ],
    )

    result = main()

    captured = capsys.readouterr()

    assert result == 0
    assert captured.out.strip() == "1.0"

def test_cli_convert_error(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.argv",
        [
            "toolkit",
            "convert",
            "1",
            "--from",
            "kg",
            "--to",
            "m",
        ],
    )

    result = main()

    captured = capsys.readouterr()

    assert result == 2
    assert "Converter error" in captured.err
