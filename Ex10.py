#10. เขียนโปรแกรมรับอินพุต 1 ตัว เป็นจำนวนเงินในหน่วยดอลล่าสหรัฐ (จำนวน)และตรวจสอบว่า จำนวนที่รับมามีค่ามากกว่า 0 หรือไม่
#	• ถ้ามีค่ามากกว่า 0 ให้คำนวณจำนวนเงินในหน่วยบาท (THB=USD*32.5) และ 
#         พิมพ์ค่าออกมา
#	• ถ้ามีค่าน้อยกว่าหรือเท่ากับ 0 ให้พิมพ์ “You don’t have money”
#
USD = int(input("กรอกจำนวนเงินUSDในบัญชี : "))

USD_to_THB = USD*32.5

if USD_to_THB > 0 :
    print(f"คุณมีเงินดอลลาร์ทั้งหมด : {USD}")
    print(f"เป็นเงินบาททั้งหมด : {USD_to_THB:.2f}")
elif USD <= 0:
    print("You don’t have money")
    print("หมดตูดแล้วพ่อหนุ่ม")