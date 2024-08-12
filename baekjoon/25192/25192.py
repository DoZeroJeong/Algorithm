from sys import stdin as s

from baekjoon.utils import _input_str


def main(questions):
    _dict = dict()

    gomgom_count = 0
    is_enter = False

    for q in questions:
        if q == "ENTER":
            is_enter = True
            _dict = {}
        else:
            is_enter = False
            if not _dict.get(q):
                gomgom_count += 1
                _dict[q] = True

    return gomgom_count


if __name__ == "__main__":
    for i in range(3):
        s = open(f"input_{i+1}.txt", "r")
        n = int(s.readline().strip())
        print(main(_input_str(n, s)))
