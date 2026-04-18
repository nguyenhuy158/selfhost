from typer.testing import CliRunner
from src.selfhost.main import app

runner = CliRunner()

def test_version():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "selfhost version" in result.stdout
