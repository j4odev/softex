n1 = complex(input('Digite o primeiro valor:'))
n2 = complex(input('Digite o segundo valor:'))
n3 = complex(input('Digite o terceiro valor:'))
def numeros_complexos(a,b):
    c = a+b
    d = a-b
    e = a*b
    f = a/b
    return c, d, e, f
numeros_complexos(n1, n2)
soma, subtracao, multiplicacao, divisao = numeros_complexos(n1, n2)
print(f'O resultado é:{soma}O número real é: {soma.real} e a imaginária é: {soma.imag}')
print(f'O resultado é:{subtracao}O número real é: {subtracao.real} e a imaginária é: {subtracao.imag}')
print(f'O resultado é:{multiplicacao}O número real é: {multiplicacao.real} e a imaginária é: {multiplicacao.imag}')
print(f'O resultado é:{divisao}O número real é: {divisao.real} e a imaginária é: {divisao.imag}')

