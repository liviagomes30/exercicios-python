lista=[]
for i in range(5):
    lista.append(float(input('Digite um número: ')))
print('O maior número digitado foi o: {}'.format(max(lista)))
print('O menor número digitado foi o: {}'.format(min(lista)))