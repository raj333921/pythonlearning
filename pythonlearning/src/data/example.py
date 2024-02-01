from asyncio import as_completed
from turtle import pd


def create_list():
    item_list = ["rajesh", "ramesh", "rakesh"]
    return item_list


item_list = create_list()
for item in item_list:
    print(item)
