#Student ka naam input lo.
#Age input lo.
#Favourite subject input lo.
#In teeno values ko ek dictionary mein store karo.
#Dictionary ko print karo.
#Check karo ke student ki age 18 ya us se zyada hai ya nahi.

# hint:
#input()
#int()
#Dictionary { }
#print()
#if / else

student = {
    "name" : input("Enter your name :"),
    "age" : int(input("Enter your age : ")),
    "favourite_subject" : input("Enter your favourite subject : ")
    
}
print("\n--- Student Information ---")
print("Name:", student["name"])
print("Age:", student["age"])
print("Favourite Subject:", student["favourite_subject"])
if student["age"] >= 18:
    print("Student is eligible")

else:
    print("Student is not eligible")