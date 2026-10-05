from random import randint

class Boss:
    
    def __init__(self, vida, nome):
        self.vida = vida
        self.nome =nome
   
    def VidaBoss(self):
        print(self.nome.center(100))
        print(f"{"█" * 100} {self.vida}%")
        print("""
           /^\/^\\
         _|__|  O|
\\/     /~     \\_/ \\
 \\____|__________/  \\
        \\_______      \\
                `\\     \\                 \\
                  |     |                  \\
                 /      /                   \\
                /     /                     \\
              /      /                       \\
             /     /                         \\
           /      /                           \\
          /     /                             \\
        /      /                               \\
       /______/                                 \\
""")
acerto = randint(0, 5)           
boss1 = Boss(100, 'python')
boss1.VidaBoss()

class jogador:
    def __init__(self, ataque):
        self.ataque = ataque

    def AtaqueBoss(self, vida , acerto):
            
            while vida >0:   
                ataque = int(input("informe um número de 0 até 5: "))
                
                if ataque == acerto:
                    vida -= 20
                    print("ACERTOU!")
                    print(f"O Boss agora tem {vida} HP")
                    print(f'{"█" * vida} {vida}%')
                    print(r"""
             *       ✦       *
          ✧      *      ✧
              /^\/^\
            _|__|  X|
      ✦  \/     /~     \_/ \     *
        \____|__________/  \
             \_______      \
                     `\     \                 \
                       |  x  |                  \
                      /  /\/  /                   \
                     /  / XX /                    \
                    /  /____/                      \
                  /      /                          \
                 /  X   /                           \
               /      /                             \
              /__/\/__/                              \
                 ||                                   
                 ||  
""")
                    acerto = randint(0, 5)
                else:
                    print("ERROU!")

            print("O Boss morreu!")


jogador1 = jogador('ataque')

jogador1.AtaqueBoss(boss1.vida, acerto)
                