#4.เขียนโปรแกรมรับ input 1 ตัว เป็นจำนวนเต็ม และตรวจสอบว่าเป็นเลขคู่ หรือ เลขคี่



Number_input = int(input("ป้อนจำนวนเต็ม : "))

if Number_input % 2 == 0 : 
    print(f"จำนวน : {Number_input} ป็นเลขคู่")
else :
     print(f"จำนวน : {Number_input} เป็นเลขคี่")