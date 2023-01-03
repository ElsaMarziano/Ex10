lst1 = [0,1,"2",3,"a"]
for a in lst1:
    try:
        print(6// int(a), end = " ")
    except ValueError:
        print("oops",end = " ")
    except ZeroDivisionError:
        print("boom",end = " ")