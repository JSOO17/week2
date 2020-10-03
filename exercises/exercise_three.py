text = "Beautiful is better than ugly"
vocals = ["a", "e", "i", "o", "u"]


def count_text():
    count = 0
    count_vocals = 0
    text_without = ""
    while text[count:len(text)]:
        if text[count] in vocals:
            text_without += "*"
            count_vocals = count_vocals + 1
        else:
            text_without += text[count]
        count = count + 1

    return count_vocals, text_without


if __name__ == '__main__':
    counts_vocals, text_without_vocals = count_text()
    print(text_without_vocals)
    print(counts_vocals)
