from unittest.mock import patch

from src.file_readers import read_csv_file, read_excel_file


@patch('builtins.open')
def test_read_csv_file_not_found(mock_open):
    """Тест: CSV файл не найден"""
    mock_open.side_effect = FileNotFoundError()
    result = read_csv_file("net_takogo.csv")
    assert result == []


@patch('pandas.read_excel')
def test_read_excel_file_works(mock_read_excel):
    """Тест: чтение Excel файла"""

    class FakeDataFrame:
        def to_dict(self, orient='records'):
            return [
                {"id": 1, "name": "Иван", "amount": 100},
                {"id": 2, "name": "Мария", "amount": 200},
            ]

    mock_read_excel.return_value = FakeDataFrame()

    result = read_excel_file("test.xlsx")

    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[0]["name"] == "Иван"
    assert result[1]["id"] == 2
    assert result[1]["name"] == "Мария"


@patch('pandas.read_excel')
def test_read_excel_file_not_found(mock_read_excel):
    """Тест: Excel файл не найден"""
    mock_read_excel.side_effect = FileNotFoundError()

    result = read_excel_file("net_takogo.xlsx")
    assert result == []


@patch('pandas.read_excel')
def test_read_excel_file_error(mock_read_excel):
    """Тест: ошибка при чтении Excel"""
    mock_read_excel.side_effect = Exception("Ошибка чтения")

    result = read_excel_file("test.xlsx")
    assert result == []
