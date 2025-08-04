#1. Convert the time entered in hh,min and sec into seconds.

#take input from user 
hh = int(input("Enter hours :"))
min = int(input("Enter minutes :"))
sec = int(input("Enter seconds :"))

#Total Seconds= (hh×3600)+(min×60)+sec 
total_seconds =(hh *3600) + (min * 60) + sec

#Display output
print(f'Total Seconds : {total_seconds} .')