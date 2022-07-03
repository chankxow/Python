#5. เขียนโปรแกรมรับตัวเลขจำนวนจริง 2 จำนวน เก็บไว้ที่ num1 และ num2
#ตรวจสอบว่า 
#	ถ้า num1>num2
#	 	ให้แสดงผลคำว่า More than
#	ถ้า num1<num2
#		ให้แสดงผลคำว่า Less than 


Num1 = int(input("ป้อนจำนวนแรก : "))
Num2 = int(input("ป้อนจำนวนที่สอง : "))

if Num1 > Num2 :
    print(f" {Num1} is more than {Num2} ")
elif Num1 < Num2 :
    print(f"{Num1} is less than {Num2}")
    