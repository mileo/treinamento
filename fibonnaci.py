#-*- coding: utf-8 -*-

def fibonacci():
    anterior = 0
    inicial = 1

    while True:
        atual = inicial + anterior
        yield atual
        anterior = inicial
        inicial = atual

f = fibonacci()

print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()

# Podemos chamar a função infinitivamente, que nossa função sempre funcionará

