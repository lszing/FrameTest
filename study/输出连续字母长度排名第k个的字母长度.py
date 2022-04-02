if __name__ == '__main__':
    dic = {"a": 3, "b": 1, "c": 1, "d": 2}
    print(sorted(dic, key=lambda x: dic[x]))
    li = ["123", "97", "5412"]
    li.sort(reverse=True)
    print(li)
