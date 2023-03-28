from random import randint
from time import sleep
computador = randint(0, 5)
print("\033[1;35m-=-" * 20)
print("\033[1;34mvou pensar em um número entre 0 e 5.")
print("\033[1;35m-=-" * 20)
sleep(2)
print("\033[1;34mTente adivinhar...")
sleep(2)
jogador = int(input("\033[1;31mEm que número eu pensei?"))
print("\033[1;34mProcessando...")
sleep(3)
if jogador == computador:
    print("\033[1;32mParabéns! você conseguiu me veenceu!")
else:
    print("\033[1;33mGanhei! eu pensei no número {} e não no {}!".format(computador, jogador))