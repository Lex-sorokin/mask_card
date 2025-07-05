from src.masks import get_mask_account, get_mask_card_number
from utils import open_json_file, transaction_amount


print(get_mask_card_number("1234 5678 1234 5678"))
print(get_mask_account("123456"))


print(transaction_amount(open_json_file('data/operations.json')[0]))
