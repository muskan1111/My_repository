call = int(input("Enter the number of calls: "))
if(call<=100):
    bill = 1.20*call

elif(call>=101 and call<=150):
    bill = 1.20*100+0.80*(call-100)

elif(call>=151 and call<=200):
    bill = 1.20*100+0.80*50+0.70*(call-150)

elif(call>200):
    bill = 1.20*100+0.80*50+0.70*50+0.60*(call-200)

print("Bill before tax is: ",bill)

bill = bill+0.10*(bill)

print("Total bill(after tax) is: ",bill)
    
