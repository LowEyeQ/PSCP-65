'''cutecat'''
def lenght(_dict, txt):
    '''lenght'''
    return len([few for few in _dict.values() if txt in few])

def main():
    '''_'''
    countable, _dict, cat_result = int(input()), {}, {}
    for _ in range(countable):
        txt = input()
        if len(txt.split('"')) > len(txt.split("'")):
            _dict[txt.split('"')[1]] = txt.split('"')[3]
        else:
            _dict[txt.split("'")[1]] = txt.split("'")[3]
    count_cat, count_fox = lenght(_dict, 'Cat'), lenght(_dict, 'Fox')
    check_cat, check_fox, count = 'Cat01' in _dict.values(), 'Fox01' in _dict.values(), 0
    if count_cat == 0 or check_cat == 0:
        cat_result['Garfield'] = 'Cat01'
    if count_fox == 0 or check_fox == 0:
        cat_result['Fubuki'] = 'Fox01'
    for key, value in sorted(_dict.items(), key=lambda x: x[1]):
        if check_fox == 0 and value.count('Fox') >= 1 and count == 0:
            count += 1
            cat_result['Fubuki'] = 'Fox01'
        cat_result[key] = value
    count_cat, count_fox = lenght(cat_result, 'Cat'), lenght(cat_result, 'Fox')
    cat, fox = {}, {}
    for key, value in cat_result.items():
        if value.count('Cat') >= 1:
            cat.update({int(value.split('Cat')[1]): [key, value]})
        elif value.count('Fox') >= 1:
            fox.update({int(value.split('Fox')[1]): [key, value]})
    print('Cat : %d\nFox : %d' % (count_cat, count_fox))
    for cry in sorted(cat):
        print(cat[cry][0] + ' : ' + cat[cry][1])
    for cry in sorted(fox):
        print(fox[cry][0] + ' : ' + fox[cry][1])
main()
