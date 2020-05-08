def digit_repeat_count(digit, from_num, to_num) :
    count = 0
    for num in range(int(from_num), int(to_num)+1):
        for d in str(num):
            if int(d) == int(digit):
                count += 1
    return count

try :
    from_num = input('From:  ')
    to_num = input('To:  ')
    digit = input('digit [to count its repeatation]:  ')
    print (digit_repeat_count(digit, from_num, to_num))

except :
    print('Expection')