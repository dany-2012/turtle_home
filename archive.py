#import random
#rand_number = random.randint(0, 100)
#print("введите число от нуля до ста: ")
#while True: бесконечный цикл
   # input_number = int(input('введите число, которое загадал компьютер: '))
   # if input_number >=100 and input_number <=0:
      #  print('вы ввели число не в звдвнных нами границах')
    #if rand_number == input_number:
        #print( "ура, вы выиграли")
       # break
    #else:
        ##list = [1, "2", 3, "4", "5", 6, 7, 8]
#list.append(10)# эта команда добавляет число или строку в конец списка
#list.remove(1)# эта команда удаляет число или строку из списка
#list.reverse()# эта команда переворачивает список
#for x in list:
    #print(x)
#import turtle

t = turtle.Turtle()


def draw_square():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)


def draw_circle():
    t.left(180)
    t.forward(100)
    t.right(45)
    t.forward(73)
    t.right(90)
    t.forward(73)


draw_square()
draw_circle()

def draw_hexagon():
    t.left(45)
    t.forward(75)
    t.forward(50)
    t.left(45)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(45)
    t.forward(50)
    t.left(45)
    t.forward(50)
    t.left(90)
    t.forward(50)

draw_hexagon()



turtle.done()
(len(list))
#    print(list[x])

list=[[], ['1*1=1',' 1*2=2', '1*3=3',' 1*4=4', '1*5=5', '1*6=6', '1*7=7', '1*8=8', '1*9=9', '1*10=10'],
          ['2*1=2', '2*2=4', '2*3=6', '2*4=8', '2*5=10', '2*6=12', '2*7=14', '2*8=16', '2*9=18', '2*10=20'],
          ['3*1=3',' 3*2=6',' 3*3=9', '3*4=12', '3*5=15', '3*6=18', '3*7=21', '3*8=24', '3*9=27', '3*10=30'],
          ['4*1=4', '4*2=8', '4*3=12', '4*4=16', '4*5=20', '4*6=24', '4*7=28', '4*8=32', '4*9=36', '4*10=40'],
          ['5*1=5', '5*2=10', '5*3=15', '5*4=20', '5*5=25', '5*6=30', '5*7=35', '5*8=40', '5*9=45', '5*10=50']]
for x in list:
        print(x)
input_number = int(input("введите число, на которое вы хотите увидеть умножение:"))
for x in list[input_number]:
    print(x)
