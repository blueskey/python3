# -*- coding: utf-8 -*-
# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

__author__ = 'Administrator'
import random

if __name__ == "__main__":
    NUM_OF_TICKET = 20
    LENGTH_OF_TICKET = 10

    char_lst = []

    def get_lst(lst, c1, c2):
        char_lst = lst[0]
        for i in range(ord(c1), ord(c2) + 1):
            char_lst.append(chr(i))

    get_lst([char_lst], '0', '9')
    get_lst([char_lst], 'a', 'z')
    get_lst([char_lst], 'A', 'Z')

    def gen_ticket():
        single_ticket_lst = [char_lst[random.randint(0, len(char_lst) - 1)]
                             for i in range(LENGTH_OF_TICKET)]

        return "".join(single_ticket_lst)

    result = set()
    while len(result) <= NUM_OF_TICKET:
        result.add(gen_ticket())

    print(result)
