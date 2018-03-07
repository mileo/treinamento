

def calcular_media():
     series = []
     def averager(novo_valor):
         series.append(novo_valor)
         total = sum(series)
         return total/len(series)
     return averager


avg = calcular_media()
print avg(10)
print avg(20)
print avg(15)
print avg(12)
print avg(10)
print avg(10)
print avg(10)