#A list contains sublist with Emp information as follows:
#Data = [[101, "Seema", 45000],  
#        [102, "Rasagn", 30000],  
#        [103, "Aman", 40000],  
#        [104, "Surest", 35000]]
 
Data = [[101, "Seema", 45000],  
        [102, "Rasagn", 30000],  
        [103, "Aman", 40000],  
        [104, "Surest", 35000]]

for i in range(len(Data)): 
    for j in range(i+1,len(Data)):
        if Data[i][2] > Data[j][2]:
            Data[i] , Data[j] = Data[j] ,Data[i]
print("Employe data stored by salary:")
for emp in Data:
    print(emp) 