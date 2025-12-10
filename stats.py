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
