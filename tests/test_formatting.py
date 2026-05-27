import pytest
from tg_bot import format_locations, format_detectives

@pytest.mark.positive
def test_format_locations_success():
    locations = [{"location": "London"}, {"location": "Paris"}]
    expected = "Доступные локации:\n\n- London\n- Paris\n"
    assert format_locations(locations) == expected

@pytest.mark.positive
def test_format_detective_success():
    detectives =  [{"detective name": "Holmes", "clue count": 5}]
    expected = 'Информация о детективах:\n\n- Детектив Holmes, улики — 5 шт.\n'
    assert format_detectives(detectives) == expected

@pytest.mark.negative
def test_format_locations_empty():
    assert format_locations([]) == "Локации не найдены"

@pytest.mark.negative
def test_format_detectives_empty():
    assert format_detectives([]) == 'Детективы не найдены'