from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    expected = "1234 56** **** 5678"
    result = get_mask_card_number("1234 5678 1234 5678")
    assert expected == result


def test_get_mask_account():
    expected = "**3456"
    result = get_mask_account("123456")
    assert expected == result
