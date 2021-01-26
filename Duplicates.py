
## Напишите функцию,
# которая на вход принимает строку, а на выходе выдаёт массив всех повторяющихся символов.
# И после напишите юнит тесты для этой функции
class Duplicates:
    def FindDuplicates(self, initialString):
        characters = {}
        for character in initialString:
            if characters.get(character,None) != None:
                characters[character] += 1
            else:
                characters[character] = 1
        outputArray = [k for k, v in characters.items() if v > 1]
        return outputArray
