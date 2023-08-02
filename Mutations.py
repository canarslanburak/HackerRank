def mutate_string(string, position, character):
    yazi=list(string)
    yazi[position]="{}".format(character)
    s="".join(yazi)
    return s


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)