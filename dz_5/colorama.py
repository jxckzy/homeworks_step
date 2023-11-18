from colorama import Fore, Back, Style, init

# initialization of colorama
init()

# some examples of using colorama
print(Fore.RED + "Цей текст буде червоного кольору")
print(Back.GREEN + "Цей текст буде на зеленому фоні")
print(Style.BRIGHT + "Цей текст буде в яскравому стилі")

# resetting all the settings to default
print(Style.RESET_ALL + "Цей текст буде в стандартних налаштуваннях")