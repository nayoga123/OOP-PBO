class Hero:
    
    __jumlah = 0

    def __init__(self, nama, health, attPower, armor):
        self.__name = nama
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor

        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level
        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def gainEXP(self):  
        pass

    @gainEXP.setter
    def gainEXP(self, addEXP):
        self.__exp += addEXP

        while self.__exp >= 100:
            self.__level += 1
            self.__exp -= 100
            print(f"{self.__name} level up!")

            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

            self.__health = self.__healthMax

    def attack(self, musuh):
        print(f"{self.__name} menyerang {musuh.__name}")  
        self.gainEXP = 50

    @property
    def info(self):
        return f"{self.__name} level {self.__level}:\n"\
               f"\thealth = {self.__health}/{self.__healthMax}\n"\
               f"\tattack = {self.__attPower}\n"\
               f"\tarmor = {self.__armor}"


if __name__ == "__main__":
    hero1 = Hero("Barges", 100, 20, 10)
    hero2 = Hero("pompa", 80, 25, 5)

    print(hero1.info)
    hero1.attack(hero2)
    hero1.attack(hero2)

    print(hero1.info)