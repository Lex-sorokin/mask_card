from src.masks import get_mask_account, get_mask_card_number
from src.utils import open_json_file, transaction_amount

if __name__ == '__main__':

    transaction_amount(open_json_file('data/operations.json')[0])
    open_json_file('data/operations.json')
    open_json_file('data/operations.json')
    open_json_file('data/operations.json')
    open_json_file('data/operations.json')
    open_json_file('data/operations.json')

    get_mask_card_number("1234 5678 1234 5678")
    get_mask_account("123456")
