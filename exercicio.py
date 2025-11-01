from os import system, name

class DivisaoPorZero(Exception):
    """Exceção para o caso do número 0 aparecer como divisor"""
    def __init__(self, n1):
        super().__init__(f"O número 0 não pode ser o divisor de um número.\nDigite outro número para dividir {n1}")

class NumeroNegativoError(Exception):
    """Exceção para um número negativo em uma operação que não o espera (adição, subtração, raíz)"""
    def __init__(self, operacao):
        super().__init__(f"A operação '{operacao}' não aceita números negativos.")

 
class Calculadora:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.resultado = None
    
    def adicao(self):
        if self.n1<0 or self.n2<0:
            raise NumeroNegativoError("adição")
        self.resultado = self.n1+self.n2
        return self.resultado
    
    def subtracao(self):
        if self.n1<0 or self.n2<0:
            raise NumeroNegativoError("subtração")
        self.resultado = self.n1-self.n2
        return self.resultado
    
    def multiplicacao(self):
        self.resultado = self.n1*self.n2
        return self.resultado
    
    def divisao(self):
        if self.n2==0:
            raise DivisaoPorZero(self.n1)
        self.resultado = self.n1/self.n2
        return self.resultado
    
    def raizQ(self):
        if self.n1<0:
            raise NumeroNegativoError("raíz quadrada")
        self.resultado = self.n1**(1/2)
        return self.resultado
    
    def raizN(self):
        if self.n1<0 or self.n2<0:
            raise NumeroNegativoError("raíz enésima")
        self.resultado = self.n1**(1/self.n2)
        return self.resultado
    
    def potencia(self):
        self.resultado = self.n1**self.n2
        return self.resultado

def cabecalho(msg, simb, esp):
    print(f" {msg} ".center(esp, simb))

def exibir_menu():
    cabecalho("CALCULADORA", "=", 35)
    print("-"*35)
    print("\n{:^30} | {:<2}".format("OPERAÇÃO", "ID"))
    print("=" * 35)
    print("{:<30} | {:<2}".format("ADIÇÃO", 1))
    print("{:<30} | {:<2}".format("SUBTRAÇÃO", 2))
    print("{:<30} | {:<2}".format("MULTIPLICAÇÃO", 3))
    print("{:<30} | {:<2}".format("DIVISÃO", 4))
    print("{:<30} | {:<2}".format("RAÍZ QUADRADA", 5))
    print("{:<30} | {:<2}".format("RAÍZ ENÉSIMA", 6))
    print("{:<30} | {:<2}".format("POTÊNCIA", 7))
    print("{:<30} | {:<2}".format("SAIR", 0))

def limpar_tela():
    system('cls' if name == 'nt' else 'clear')

def ler_numero(msg):
    while True:
        entrada = input(msg)
        if '/' in entrada:
            print("ATENÇÃO: Não são permitidas frações. Digite um número decimal ou inteiro.")
            continue
        try:
            return float(entrada)
        except ValueError:
            print("ATENÇÃO: Digite um número válido (ex: 2 ou 0.5).")



def main():
    while True:
        limpar_tela()
        while True:
            exibir_menu()
            try:
                escolha = int(input("--> "))
                if escolha < 0 or escolha > 7:
                    print("ATENÇÃO: Escolha uma das alternativas oferecidas pelo menu. Digite novamente.")
                elif escolha == 0:
                    print(f"{' Até mais! ':-^35}")
                    return
                else:
                    break
            except ValueError:
                print("ATENÇÃO: Você deve inserir um número inteiro para escolher. Digite novamente.")
        
        if escolha == 1:
            limpar_tela()
            cabecalho("ADIÇÃO", "=", 35)
            print("-"*35)
            n1 = ler_numero("Digite o primeiro número: ")
            n2 = ler_numero("Digite o segundo número: ")
            try:
                res = Calculadora(n1, n2).adicao()
                limpar_tela()
                cabecalho("ADIÇÃO", "=", 35)
                print("-"*35)
                s1 = str(n1)
                s2 = str(n2)
                sr = str(res)
                largura = max(len(s1), len(s2), len(sr)) + 2
                print()
                print(s1.rjust(largura))
                print("+ " + s2.rjust(largura - 2))
                print("-" * largura)
                print(sr.rjust(largura))
            except Exception as e:
                print(f"\nErro: {e}")
            input("\nPressione ENTER para continuar...")

        elif escolha == 2:
            limpar_tela()
            cabecalho("SUBTRAÇÃO", "=", 35)
            print("-"*35)
            n1 = ler_numero("Digite o primeiro número: ")
            n2 = ler_numero("Digite o segundo número: ")

            try:
                res = Calculadora(n1, n2).subtracao()
                limpar_tela()
                cabecalho("SUBTRAÇÃO", "=", 35)
                print("-"*35)
                s1 = str(n1)
                s2 = str(n2)
                sr = str(res)
                largura = max(len(s1), len(s2), len(sr)) + 2
                print()
                print(s1.rjust(largura))
                print("- " + s2.rjust(largura - 2))
                print("-" * largura)
                print(sr.rjust(largura))
            except Exception as e:
                print(f"\nErro: {e}")
            input("\nPressione ENTER para continuar...")
        
        elif escolha == 3:
            limpar_tela()
            cabecalho("MULTIPLICAÇÃO", "=", 35)
            print("="*35)
            n1 = ler_numero("Digite o primeiro número: ")
            n2 = ler_numero("Digite o segundo número: ")

            try:
                res = Calculadora(n1, n2).multiplicacao()
                limpar_tela()
                cabecalho("MULTIPLICAÇÃO", "=", 35)
                print("-"*35)
                s1 = str(n1)
                s2 = str(n2)
                sr = str(res)
                largura = max(len(s1), len(s2), len(sr)) + 2
                print()
                print(s1.rjust(largura))
                print("X " + s2.rjust(largura - 2))
                print("-" * largura)
                print(sr.rjust(largura))
            except Exception as e:
                print(f"\nErro: {e}")
            input("\nPressione ENTER para continuar...")

        elif escolha == 4:
            limpar_tela()
            cabecalho("DIVISÃO", "=", 35)
            print("="*35)
            n1 = ler_numero("Digite o dividendo: ")
            n2 = ler_numero("Digite o divisor: ")

            try:
                res = Calculadora(n1, n2).divisao()
                limpar_tela()
                cabecalho("DIVISÃO", "=", 35)
                print("-"*35)
                s1 = str(n1)
                s2 = str(n2)
                sr = str(res)
                largura = max(len(s1), len(s2), len(sr)) + 2
                print()
                print(s1.rjust(largura))
                print("/ " + s2.rjust(largura - 2))
                print("-" * largura)
                print(sr.rjust(largura))
            except Exception as e:
                print(f"\nErro: {e}")
            input("\nPressione ENTER para continuar...")

        elif escolha == 5:
            limpar_tela()
            cabecalho("RAÍZ QUADRADA", "=", 35)
            print("="*35)
            n1 = ler_numero("Digite o número: ")

            try:
                res = Calculadora(n1, None).raizQ()
                limpar_tela()
                cabecalho("RAÍZ QUADRADA", "=", 35)
                print("-"*35)
                s1 = str(n1)
                sr = str(res)
                largura = max(len(s1), len(sr)) + 2
                print()
                print(f"√({s1})".rjust(largura))
                print("-" * largura)
                print(sr.rjust(largura))
            except Exception as e:
                print(f"\nErro: {e}")
            input("\nPressione ENTER para continuar...")

        elif escolha == 6:
            limpar_tela()
            cabecalho("RAÍZ ENÉSIMA", "=", 35)
            print("="*35)
            n1 = ler_numero("Digite o número base: ")
            n2 = ler_numero("Digite o índice da raíz: ")

            try:
                res = Calculadora(n1, n2).raizN()
                limpar_tela()
                cabecalho("RAÍZ ENÉSIMA", "=", 35)
                print("-"*35)
                s1 = str(n1)
                s2 = str(n2)
                sr = str(res)
                largura = max(len(s1), len(s2), len(sr)) + 4
                print()
                print(f"{s2}√({s1})".rjust(largura))
                print("-" * largura)
                print(sr.rjust(largura))
            except Exception as e:
                print(f"\nErro: {e}")
            input("\nPressione ENTER para continuar...")

        elif escolha == 7:
            while True:
                try:
                    limpar_tela()
                    cabecalho("POTÊNCIA", "=", 35)
                    print("="*35)
                    n1 = ler_numero("Digite a base: ")
                    n2 = ler_numero("Digite o expoente: ")

                    res = Calculadora(n1, n2).potencia()
                    limpar_tela()
                    cabecalho("POTÊNCIA", "=", 35)
                    print("-"*35)
                    s1 = str(n1)
                    s2 = str(n2)
                    sr = str(res)
                    largura = max(len(s1), len(s2), len(sr)) + 4
                    print()
                    print(f"{s1}^{s2}".rjust(largura))
                    print("-" * largura)
                    print(sr.rjust(largura))
                    break  # sai do loop após sucesso
                except Exception as e:
                    print(f"\nErro: {e}")
                    input("\nPressione ENTER para tentar novamente...")
            input("\nPressione ENTER para continuar...")



if __name__ == "__main__":
    main()