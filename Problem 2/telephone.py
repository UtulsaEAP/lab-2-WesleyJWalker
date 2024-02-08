def telephone():
    phone_number = int(input())
    end = str(phone_number % 10000)
    x = phone_number // 10000
    mid = str(x % 1000)
    beg = str(phone_number // 10000000)
    print("(" + beg + ") " + mid + "-" + end)
    
if __name__ == "__main__":
    telephone()