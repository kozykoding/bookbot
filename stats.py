def text_count(file_contents):
    texts = len(file_contents.split())
    return texts


def character_count(file_contents):
    characters = {}
    for ch in file_contents.lower():
        if ch in characters:
            characters[ch] = characters[ch] + 1
        else:
            characters[ch] = 1
    return characters


def sort_helper(item):
    return item["num"]


def sorted_ch(file_contents):
    chars = character_count(file_contents)
    list_of_dicts = []
    for ch, count in chars.items():
        dict = {
            "char": ch,
            "num": count,
        }
        list_of_dicts.append(dict)
    list_of_dicts.sort(reverse=True, key=sort_helper)
    return list_of_dicts
