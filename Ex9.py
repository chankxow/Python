
FHR = int(input("กรอกจำนวนอุณหภูมิ : " ))

C = (5*(FHR-32))/9

if FHR >= 32 :
    print("'อุณหภูมิคือ {C:.2f} องศา")
elif FHR < 32 :
    print(f"อุณหภูมิคือ {C:.2f} องศา")
    print("IS SO COLD!!!!")