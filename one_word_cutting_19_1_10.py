import codecs

# 大ファイルを扱うので、メモリ溢れ対策に、１行ずつ読んで結果ファイルに追記していく。
with open("ItiGyouGotoKiji.txt") as f:
    for line in f.readlines():
        chars = [c for c in line if c != u" "]
        with codecs.open("allWiki_1kugiri.txt", "a", "utf-8") as newf:
            newf.write(u" ".join(chars))

