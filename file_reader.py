file_name = 'file_reader.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
pi_string = ''    
for line in lines:
      pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))



print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
     break
    second_number = input("Second number: ")
    try:
          answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("you cann't divide by zero")
    else:
        print(answer)