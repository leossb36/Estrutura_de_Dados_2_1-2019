from timeit import default_timer as timer
import random

def simpleSearch(vector):
    print("Valores: " + str(vector))
    numSearch = input('Qual valor desejado? ')
    start_time = timer()
    for i in range(len(vector)):
        if(numSearch == str(vector[i])):
            end_time = timer()
            delta = end_time - start_time
            print('tempo gasto: %s sec\n' % delta + 'posição: %s\n'  % str(i))
        

def binarySearch(vector, low, high, numSearch):
    start_time = timer()

    while low <= high: 
        mid = low + (high - low)/2;
        mid = int(mid)
        # se estiver no meio 
        if vector[mid] == numSearch: 
            end_time = timer()
            delta = end_time - start_time
            print('Valor encontrado')
            print('tempo gasto: %s sec\n' % delta)
            return mid 
        # se estiver na parte maior do vetor 
        elif vector[mid] < numSearch: 
            low = mid + 1 # incrementa
        # se estiver na parte menor do vetor 
        else: 
            high = mid - 1 #decrementa
    print('Valor não encontrado')
    return -1

def interpolationSearch(vector):
    start_time = timer()
    sup_limit = vector[len(vector) - 1]
    inf_limit = vector[0]
    print("Valores: " + str(vector))
    numSearch = int(input('Qual valor desejado? '))

    median = inf_limit + (sup_limit - inf_limit) * ((numSearch - vector[0])/((vector[len(vector) - 1]) - vector[0]))
    median = int(median)
    i = 0

    if( numSearch == median):
        end_time = timer()
        delta = end_time - start_time
        while i != vector[median]:
            i += 1
        print('tempo gasto: %s sec\n' % delta + 'posição: %s\n'  % str(i))
    else:
        return print('Valor não encontrado!')

def selectionSort(vector):
    for i in range(len(vector)):
        iMin = i
        for j in range(i+1, len(vector)):   
            if(vector[iMin] > vector[j]):
                iMin = j
        vector[i], vector[iMin] = vector[iMin], vector[i]
            
def setRange(vector):
    iF = int(input('Defina a quantidade de elementos da lista: '))
    while len(vector) < iF:
          rnd = random.randint(0, iF - 1)
          if rnd in vector:
              continue
          else:
              vector += [rnd]
    return iF

vector = []
setRange(vector)

def menu():
    print("-----------------------------------------------------")
    print("\t\t\tMENU")
    print("-----------------------------------------------------")
    print("1 - Busca sequencial simples") # precisa ser ordenado pra dar certo
    print("2 - Busca sequencial simples sem ordenamento") # precisa ser ordenado pra dar certo
    print("3 - Busca sequencial binaria") # nao necessariamente
    print("4 - Busca sequencial binaria sem ordenamento") # nao necessariamente
    print("5 - Busca sequencial interpolação") # nao necessariamente
    print("6 - Busca sequencial interpolação sem ordenamento") # nao necessariamente
    print("0 - Sair")
    print("-----------------------------------------------------")
    opt = input("Digite uma Opção: ")
    return opt

opt = 0
while opt != '6':
    opt = menu()
    if opt == '1':
        selectionSort(vector)
        simpleSearch(vector)
    elif opt == '2':
        random.shuffle(vector)
        simpleSearch(vector)
    elif opt == '3':
        selectionSort(vector)
        print("Valores: " + str(vector))
        numSearch = int(input('Qual valor desejado? '))
        response = binarySearch(vector, vector[0], len(vector) - 1, numSearch)
        print('posição: %s\n'  % response)
    elif opt == '4':
        random.shuffle(vector)
        print("Valores: " + str(vector))
        numSearch = int(input('Qual valor desejado? '))
        response = binarySearch(vector, vector[0], vector[len(vector) - 1], numSearch)
        print('posição: %s\n'  % response)
    elif opt == '5':
        selectionSort(vector)
        interpolationSearch(vector)
    elif opt == '6':
        random.shuffle(vector)
        interpolationSearch(vector)
    elif opt == '0':
        print('\n' + 'Obrigado =)' + '\n' + 'Leonardo dos Santos' + '\n' + 'João de Assis')
        break
    else:
        print('Opção Invalida!')
        break
