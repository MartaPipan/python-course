import pytest
from hw_08_prystatska.study_tools.formatting import format_report  


def test_format_report_success():
    #число форматується з 2 знаками після коми (.2f)
    result = format_report("Середнє", 2.5)
    expected = "--- РЕЗУЛЬТАТ [Середнє] ---\nРозраховане значення: 2.50\n---------------------------------"
    assert result == expected

def test_format_report_with_none():
    # Тест для перевірки помилки
    result = format_report("Вказана сума", None)
    expected = "== Помилка обчислення для: Вказана сума (отримано None) =="
    assert result == expected

def test_format_report_rounding():
    # чи правильно округлюється число з багатьма знаками після коми
    result = format_report("Clamp", 12.3456)
    #12.3456 має округлитися специфікатору :.2f
    assert "Розраховане значення: 12.35" in result 
