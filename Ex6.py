#6. เขียนโปรแกรมรับตัวเลข 1 ตัว ที่เป็นจำนวนเต็ม และตรวจสอบว่าจำนวนที่รับมา มีค่ามากกว่า 0 น้อยกว่า 0 หรือ เท่ากับ 0
#	ถ้ามีค่ามากกว่า 0 ให้ตรวจสอบว่าเป็นเลขคู่หรือเลขคี่
#		ถ้าเป็นเลขคู่ให้พิมพ์ “Positive even”
#ถ้าเป็นเลขคี่ให้พิมพ์ “Positive odd”
#ถ้ามีค่าน้อยกว่า 0 ให้ตรวจสอบว่าเป็นเลขคู่หรือเลขคี่
#	ถ้าเป็นเลขคู่ให้พิมพ์ “Negative even”
#ถ้าเป็นเลขคี่ให้พิมพ์ “Negative odd”
#
#ถ้าเป็นเลข 0 ห้พิมพ์ “zero”


Number = int(input("กรุณาป้อนตัวเลข : "))

if Number > 0 :
    if Number  % 2 == 0 :
            print(f"{Number} is positive even ")
    else :
        print(f"{Number} is positive odd ")
        
if Number < 0 :
    if Number % 2 == 0 :
        print(f"{Number} is Negative even ")
    else :
        print(f"{Number} is Negative odd ")
        
if Number == 0 :
     print("Zero!!!!!!!!!!") 
    
