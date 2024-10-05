
def GenerateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"
    
    with open(f"Tables/Table_{n}.txt", 'w') as file: # To edit from a folder
        file.write(table)


for i in range(1, 21):
    GenerateTable(i)

#========================================================================================