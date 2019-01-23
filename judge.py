joyo_kanji = "..."
gengo = "..."


# 2文字か
def is_2word(is_era_name):
    if len(is_era_name) == 2:
        return True
    return False


# 常用漢字か
def is_joyo_kanji(is_era_name):
    one = is_era_name[:1]
    two = is_era_name[1:]
    if one in joyo_kanji and two in joyo_kanji:
        return True
    return False
