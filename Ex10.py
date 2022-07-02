
USD = int(input("กรอกจำนวนเงินUSDในบัญชี : "))

USD_to_THB = USD*32.5

if USD_to_THB > 0 :
    print(f"คุณมีเงินUSDทั้งหมด : {USD}")
    print(f"เป็นเงินบาททั้งหมด : {USD_to_THB:.2f}")
elif USD <= 0:
    print("You don’t have money")
    print("หมดตูดแล้วพ่อหนุ่ม")