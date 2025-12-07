from model.item import Item
from datetime import datetime

def get_mock_items() -> list[dict]:
    items = []
    for i in range(10):
        item = Item(
            id = i,
            datetime_string = datetime.now(),
            user_id = i,
            n_good = i,
            n_bad = i,
            title = "Title_{}".format(i),
            tags = ["something_{}".format(i), "something_{}".format(i * 2), "something_{}".format(i * 6), ],
            link_url =  "https://www.youtube.com/watch?v=fcV-5dIRO1o",
            thumbnail_url =   "https://i3.ytimg.com/vi/fcV-5dIRO1o/hqdefault.jpg",
            description =  'Description.',
            embedded_url  =  None,
        )
        modified_item = item.toDict()
        items.append(modified_item)
    return items