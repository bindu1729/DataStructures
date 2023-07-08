#let us say your expenses for every month are as follows:
# Jan - 2200
# Feb - 2300
# March - 5000
# April - 2300

exp_1 = [["jan",2200],["feb",2300],["march",5000],["april",2300]]

exp_2_a = ["jan","feb","march","apr"]
exp_2_b = [2200,2300,5000,2300]

#0 as jan as 12 mon in year
exp_3 = [2200,2300,5000,2300]

#Q1
print("Extra amount in march compared to feb",exp_3[2]-exp_3[1])

#to print $ , comma works but use f string in diff version

print(f"Extra amount in march compared to feb {exp_3[2]-exp_3[1]} $")

#Q2
print("Avg money spent for month")

#sum of all elements / total number of elements

sum = 0
for elem in exp_3:
    sum += elem

print(f"Avg money spent for month {sum/len(exp_3)} $")

#Q3 total amount of money spent during this period
print(f"total amount of money spent during this period {sum} $")

#Q4 append may month 2000

exp_3.append(2000)
print(f"with may expenses:{exp_3}")

#Q5 return 200

print(f"march expenses {exp_3[2]-200}")
#but it return old value so assign it

exp_3[2] -= 200
print(f"march expenses {exp_3[2]}")
