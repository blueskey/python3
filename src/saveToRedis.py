# -*- coding: utf-8 -*-
# __author__ = 'Administrator'

import redis

if __name__ == "__main__":
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    user = r.get("user")
    print(user)

    # r.append("user","我是新加的")
    # user=r.get("user")
    # print(user)

    r.lpush("list", 1)
    r.lpush("list", 2)
    print(r.lrange("list", 0, -1))

    print("---------所有key:----------------")
    print(r.keys("*"))

    print("---------sorted sets:----------------")
    r.zadd("sortedSets", 1, "bcds")
    r.zadd("sortedSets", 2, "acds")
    r.zadd("sortedSets", 3, "abds")
    r.zadd("sortedSets", 4, "abds")
    r.zadd("sortedSets", 5, "aaa", 6, "ddd")

    print("sortedSets不作处理显示：\n" + str(r.zrange("sortedSets", 0, -1)))
    print("sortedSets按顺序显示：\n" + str(r.zrange("sortedSets", 0, -1, "WITHSCORES")))

    print("--------- sets:----------------")
    r.sadd("mysets", "set1")
    r.sadd("mysets", "set2", "set3", "set0")
    r.sadd("mysets", "aet1")
    print("mysets中所有的key:\n" + str(r.smembers("mysets")))
    print("mysets集合中元素数量\n" + str(r.scard("mysets")))
