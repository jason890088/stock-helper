import json
import os
import sys

import django

# use django ORM to setup socks
sys.path.append("../stock_helper")
os.environ["DJANGO_SETTINGS_MODULE"] = "stock_helper.settings"
django.setup()

from stock_manager.models import Stock


def main():
    with open("./STOCK_DAY_ALL.json") as json_file:
        all_stocks = json.load(json_file)

    for stock in all_stocks:
        s = Stock(code=stock.get("Code"), name=stock.get("Name"))
        s.save()


if __name__ == "__main__":
    main()
