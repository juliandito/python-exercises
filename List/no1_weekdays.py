def get_name(d):
    # Deklarasi konstanta
    DAY1 = "Sunday"
    DAY2 = "Monday"
    DAY3 = "Tuesday"
    DAY4 = "Wednesday"
    DAY5 = "Thursday"
    DAY6 = "Friday"
    DAY7 = "Saturday"
    # Isi listnya
    mylist = [
        None,
        DAY1,
        DAY2,
        DAY3,
        DAY4,
        DAY5,
        DAY6,
        DAY7,
    ]
    # return
    return mylist[d]

#pake for buat manggil fungsinya berulang
for i in range(1,8):
    print(get_name(i))