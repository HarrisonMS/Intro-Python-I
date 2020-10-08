# from datetime import date
#
# today = date.today()
# curr_year = date.year
# print(type(curr_year))
#
# from datetime import datetime
#
# # current date and time
# now = datetime.now()
# #
# # t = now.strftime("%H:%M:%S")
# # s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# curr_year = now.strftime("%Y")
# year_num = int(curr_year)
# birth_year = input('what year were you born')
# birth_year_num = int(birth_year)
#
# difference = year_num - birth_year_num
# print(f"your age is: {difference}")

def fibonSeq(max_num):
    seq = [0, 1]

    while seq[-1] < max_num:
        print(f"{seq[-1]} < {max_num}")
        seq.append(seq[-2] + seq[-1])
    return seq

print(fibonSeq(66))