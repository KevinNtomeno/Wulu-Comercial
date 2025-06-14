from math import sqrt as raiz

print('Equação do Segundo Grau')
print(' ')
a = int(input('Digite o valor de A: '))
b = int(input('Digite o Valor de B: '))
c = int(input('Digite o valor de C: '))
print(f'EQUAÇÃO: {a}x² {b}x {c} = 0')
delta =  (b**2) - (4*a*c)
print('DELTA: {}'.format(delta))

if delta < 0:
    print('A EQUAÇÃO NÃO TEM SOLUÇÃO!')

if delta == 0:
    print(f'''
       -b          - {b}               -{b}
x = -------- ==> ---------- ==> x = ----------
      2.a          2 x {a}            {2*a}

x = {- (b) * (2*a)}
''')
    
if delta > 0:
    raiz = raiz(delta)
    print(f'''

        {-b} +- √{delta}      
x = ----------------------
            2 x {a}

        {-b} +- {raiz}      
x = ----------------------
             {2*a}

            
        {-b} + {raiz}               {-(b) + raiz}             
x1 = ---------------==> x1 = ---------------- ==> x1 = {(-(b) + raiz) / (2 * a) }
            {2 * a}                       {2 * a}


        
        {-b} - {raiz}                    {-(b) - raiz}             
x2 = ------------------ ==> x2 = ----------------- ==> x2 = {(-(b) - raiz) / (2 * a)}
            {2 * a}                        {2 * a}
''')