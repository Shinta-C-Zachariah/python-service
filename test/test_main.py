from service.main import run_service

def test_run_service(capsys):
    run_service()
    captured = capsys.readouterr()
    assert "2 + 3 = 5" in captured.out
