class House:
    def __init__(self , name , number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self , floor):
        if int(floor) > self.number_of_floors:
            print(f'Этаж {floor} не существует в {self.name}')
        if int(floor) in range(1 , int(self.number_of_floors)):
            for i in range(1 , floor+1):
                print(i)
        if int(floor) < -1:
            print(f'Этаж {floor} не существует в {self.name}')
        if floor == 0:
            print("зачем???")



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
h2.go_to(0)
h1.go_to(-5)