names = ['Andrey','Vasiliy','Sergey','Anton','Ruslan','Evgeniy']
salary = [50000, 25000, 3000, 25020, 6050500, 7810000]
dictionary = dict(zip(names,salary))
with open('salary.txt','w+',encoding='utf-8') as file:
    for key, value in dictionary.items():
        file.write(f'{key} - {value}\n')
with open('salary.txt',encoding='utf-8') as file:
    for line in file:
        sline = line.strip()
        sline = sline.split(' - ')
        zarplata = int(sline[1]) * 0.87
        if zarplata <= 50000:
            name = sline[0].upper()
            print(f'{name} - {zarplata}')





