import time

def flush_str(str_,time_len):
    for i in str_:
        print(i,end = '',flush = True)
        time.sleep(time_len)
    print("\r")
    time.sleep(0.5)

#flush_str("*********挖宝结束了💦..*********",0.02)