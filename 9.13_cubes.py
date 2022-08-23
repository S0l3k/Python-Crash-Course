from random import randint

class Die():
    """6-гранный кубик, бросок"""

    def roll_die(self, sides=6):
        """Кидаю кубик"""

        number = 1
        print('\n', sides,'гранный кубик:\n')

        while number <= 10:

            print(f"{number}-ый бросок =", randint(1, sides))
            number += 1

cubes6 = Die()

cubes6.roll_die()
cubes6.roll_die(10)
cubes6.roll_die(20)