from time import sleep
from math import sqrt
print("LEI DE OHM -- SEGUNDA e PRIMEIRA")
print(' ')

op = int(input('''PRIMEIRA OU SEGUNDA LEI?
1 -- PRIMEIRA
2 -- SEGUNDA 
--> '''))
if op == 2:
    formula = int(input('''OQUE VOCÊ QUER CALCULAR?
    1 -- Resistência
    2 -- Registividade
    3 -- Área de sessão transversal
    4 -- Comprimento
    ------>  '''))

    sleep(1)
    # RESISTENCIA
    if formula == 1:
        def resistencia():
            print(' ')
            print('CALCULANDO RESISTENCIA')
            p = float(input('Digite o valor da Registividade: '))
            A = float(input('Digite o Valor da Área da sessão transversal: '))
            l = float(input('Digite o Comprimento: '))
            R = (p * A) / (l)
            sleep(0.5)
            print('Calculando...')
            print(f''' 
        
    Dados       |    Fórmula
                |          l
    p = {p}ohm.m|   R = p ------
    A = {A}m²   |          A
    l = {l}m    |
    R -- ?      |

            
                        Solução

            
        {p}ohm.m x {l}m             {p*l}
    R = ------------------ => R = ----------------- => R = {R:.2f}
            {A}m²                    {A}m²''')
        resistencia()


    # REGISTIVIDADE
    if formula == 2:
        def registividade():
            print(' ')
            print('CALCULANDO A REGISTIVIDADE')
            R = float(input('Digite o valor da Resistêcia: '))
            A = float(input('Digite o Valor da Área da sessão transversal: '))
            l = float(input('Digite o Comprimento: '))
            p = (R * A) / l
            print(f''' 
        
    Dados        |    Fórmula
                |          A
    R = {R}ohm  |   p = R ------
    A = {A}m²    |          l
    l = {l}m    |
    p -- ?       |

            
                        Solução

            
            {R}ohm x {A}m²               {R*A}
    p = ------------------ => p = ----------------- => p = {p:.2f} ohm.m
            {l}m                      {l}m''')
        registividade()


    # AREA DA CESSAO TRANSVERSAL
    if formula == 3:
        def Area():
            print(' ')
            print('CALCULANDO A AREA')
            R = float(input('Digite o valor da Resistêcia: '))
            p = float(input('Digite o Valor da Registividade:  '))
            l = float(input('Digite o Comprimento: '))
            A = (p * l) / R
            print(f''' 
        
    Dados        |    Fórmula
                |          l
    R = {R}ohm  |   A = p ------
    p = {p}    |            R
    l = {l}m    |
    A -- ?       |

            
                        Solução

            
            {p}ohm.m x {l}m              {R*A}
    A = ------------------ => A = ----------------- => A = {A:.2f}m²
            {R}                     {R}m''')
        Area()

    if formula == 4:
        def comprimento():
            print(' ')
            print('CALCULANDO O COMPRIMENTO')
            R = float(input('Digite o valor da Resistêcia: '))
            A = float(input('Digite o Valor da Área da sessão transversal: '))
            p = float(input('Digite o valor da Registividade: '))
            l = (R * A) / p
            print(f''' 
        
    Dados        |    Fórmula
                |          A
    R = {R}ohm  |   l = R ------
    A = {A}m²    |          p
    p = {p}     |
    l -- ?       |

            
                        Solução

            
            {R}ohm x {A}m²               {R*A}
    l = ------------------ => l = ----------------- => l = {l:.2f}m
            {p}ohm.m                 {p}ohm.m''')
        comprimento()

if op == 1:
    print('PRIMEIRA LEI DE OHM')
    print(' ')
    op1 = int(input('''QUE ELEMNTO VOCÊ QUER CALCULAR?
    1 -- RESISTÊNCIA
    2 -- INTENSIDADE
    3 -- TENSÃO
    4 -- POTÊNCIA DISSIPADA
    -->  '''))
    if op1 == 1:
        def resistencia():
            print('Calculando a Resitência')
            print(' ')
            op2 = int(input('''QUAL O TIPO DE RESISTÊCIA?
        1 -- CIRCUITO EM SÉRIE
        2 -- CIRCUITO PARALELO
        3 -- RESISTÊNCIA APENAS '''))
            if op2 == 3:
                U = float(input('Digite o Valor da Tensão: '))
                I = float(input('Digite o Valor da Intensidade: '))
                R = U / I
                print(f'''DADOS

            U = {U}
            I = {I}
            R -- ? 
                FORMULA E SOLUÇÃO
                  U
            R = -------
                  I

                   {U}
            R = -------- => R = {R}
                   {I}
                ''')
            if op2 == 1:
                def serie():
                    UF = 0
                    print('CIRCUITO EM SERIE')
                    print('  ')
                    US = int(input('Quantas TENSÃO você recebeu? '))
                    print(f'Certo, {US} Tensões')
                    for kv in range(1, US+1):
                        U = int(input(f'Digite a {kv} Tensão: '))
                        UF += U
                    print(f'UF = {UF}V')
                    print(' ')
                    I = float(input('Digite o valor da Intensidade: '))
                    R = UF / I
                    print(f'''          DADOS

            UF = {UF}V
            I = {I}A
            R -- ? 
                FORMULA E SOLUÇÃO
                  UF
            R = -------
                  I

                   {UF}
            R = -------- => R = {R}
                   {I}
                ''')

                serie()
            if op2 == 2:
                def paralelo():
                    print('CIRCUITO PARALELO')
                    print(' ')
                    UF = 0
                    US = int(input('Quantas TENSÃO você recebeu? '))
                    print(f'Certo, {US} Tensões')
                    for kv in range(1, US+1):
                        U = int(input(f'Digite a {kv} Tensão: '))
                        UF += U
                    print(f'UF = {UF/kv:.2f}V')
                    print(' ')
                    I = float(input('Digite o valor da Intensidade: '))
                    R = (UF/kv) / I
                    print(f'''          DADOS

            UF = {UF/kv:.2f}V
            I = {I}A
            R -- ? 
                FORMULA E SOLUÇÃO
                  UF
            R = -------
                  I

                   {UF/kv:.2f}
            R = -------- => R = {R}
                   {I}
                ''')
                paralelo()

        resistencia()
    if op1 == 2:
        def intensidae():
            print('CALCULANDO INTENSIDADE')
            print(' ')
            U = float(input('Digite o Valor da Tensão: '))
            R = float(input('Digite o valor da Resistência: '))
            I = U / R
            print(f'''DADOS

            U = {U}V
            R = {R} ohm
            I -- ?
                FORMULA E SOLUÇÃO
                  U
            I = -------
                  R

                   {U}V
            I = -------- => I = {I}A
                   {R} ohm
                ''')
        intensidae()
    if op1 == 3:
        def tensao():
            print(' ')
            op2 = int(input('''QUAL O TIPO DE TENSÃO?
        1 -- CIRCUITO EM SÉRIE
        2 -- CIRCUITO PARALELO
        3 -- TENSÃO APENAS 
        --> '''))
            if op2 == 3:
                R = float(input('Digite o Valor da Resistência: '))
                I = float(input('Digite o Valor da Intensidade: '))
                U = R * I
                print(f'''DADOS

            R = {R} ohm
            I = {I} A
            U -- ? 
                FORMULA E SOLUÇÃO
                  
                U = R * I 

            U = {R} x {I} => U = {U}
                ''')
            if op2 == 1:
                def serie():
                    RF = 0
                    print('CIRCUITO EM SERIE')
                    print('  ')
                    RS = int(input('Quantas RESISTÊNCIAS você recebeu? '))
                    print(f'Certo, {RS} RESISTENCIAS')
                    for kv in range(1, RS+1):
                        R = int(input(f'Digite a {kv} Resistência: '))
                        RF += R
                    print(f'RF = {RF} ohm')
                    print(' ')
                    I = float(input('Digite o valor da Intensidade: '))
                    U = RF * I
                    print(f'''          DADOS

            RF = {RF} ohm
            I = {I}A
            U -- ? 
                FORMULA E SOLUÇÃO
                  
            U = R * I

            U = {RF} x {I} => U = {U}
                ''')

                serie()

            if op2 == 2:
                def paralelo():
                    RF = 0
                    print('CIRCUITO EM PARALELO')
                    print('  ')
                    RS = int(input('Quantas RESISTÊNCIAS você recebeu? '))
                    print(f'Certo, {RS} RESISTENCIAS')
                    for kv in range(1, RS+1):
                        R = int(input(f'Digite a {kv} Resistência: '))
                        RF += R
                    print(f'RF = {RF/kv} ohm')
                    print(' ')
                    I = float(input('Digite o valor da Intensidade: '))
                    U = (RF/kv) * I
                    print(f'''          DADOS

            RF = {RF/kv} ohm
            I = {I}A
            U -- ? 
            FORMULA E SOLUÇÃO
                  
            U = R * I

            U = {RF/kv} x {I} => U = {U}V
                ''')
                paralelo()
        tensao()

    if op1 == 4:
        op2 = int(input('''ESCOLHA: 
    1 -- POTÊNCIA DISSIPADA
    2 -- RESISTÊNCIA
    3 -- INTENSIDADE
    -->  '''))
        if op2 == 1:
            def potencia():
                print('POTÊCIA DISSIPADA')
                print(' ')
                I = float(input('Digite o Valor da Intensidade: '))
                R = float(input('Digite o valor da Resistencia: '))
                P = (I*I) * R
                print(f'''                      DADOS
                I = {I}A
                R = {R} ohm
                P -- ?

                FORMULA E SOLUCÃO
                    
                P = I² x R

                P = {I} x {R}
                P = {I*I} x {R}
                P = {P}W''')
            potencia()

        if op2 == 2:
                def resistencia():
                    print('RESISTÊNCIA')
                print(' ')
                P = float(input('Digite o Valor da Potência: '))
                I = float(input('Digite o valor da Intensidade: '))
                R = P / (I*I)
                print(f'''                      DADOS
                I = {I}A
                P = {P}W
                R -- ?

                FORMULA E SOLUCÃO
            
                        P
                R = -----------
                        I²

                        {P} W             {P}
                R = ----------- => R = ---------- => R = {R}
                        {I} A            {I*I}
                        ''')
                resistencia()

        if op2 == 3:
                def intensidade():
                    print('''
                    CALCULANDO INTENSIDADE
                        
                        ''')
                P = float(input('Digite o Valor da Potência: '))
                R = float(input('Digite o valor da Resistência: '))
                I = P / R
                print(f'''                      DADOS
                R = {I} ohm
                P = {P} W
                I -- ?

                FORMULA E SOLUCÃO
            
                        P
                I² = -----------
                        R

                        {P} W               {P}
                I² = ----------- => I² = ---------- => I = √{I:.2f} => I = {sqrt(I)}
                        {R} ohm             {R}
                        ''')
                intensidade()

print('Feito por Ndombele Kevin')