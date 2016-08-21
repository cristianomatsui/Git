# #def read_file(instance, num, tipo):

print("Informe o nome da instancia")
instance = input()

file = open(instance, 'r')
print('File opened')

line = file.readline()

# Leitura dos parâmetros N e WeightType
while 'Distance' not in line:

    if 'N: ' in line:
        (aux, num_Nodes) = line.split(" ")
        num_Nodes = int(num_Nodes)
        num = num_Nodes
        print(num)
        
    if 'edgeWeightType: ' in line:
        (aux, weightType) = line.split(" ")      
        weightType = weightType.replace('\n', '').replace('\r', '')     
        tipo = weightType
        print(tipo)

    line = file.readline()

# Criação da matriz de adjacência
Matrix = [0 for x in range(num)]
for x in range(num):
    line = file.readline()
    line = line.split(" ",num)
    del line[num]
    Matrix[x] = line


# Criação do vetor de demanda
line = file.readline()
while line:

    if 'Demand' in line:
        line = file.readline()
        line = line.split(" ",num)
        del line[num]
        Demand = line
        print (Demand)

    if 'Draft' in line:
        line = file.readline()
        line = line.split(" ", num)
        del line[num]
        Draft = line
        print(Draft)

    line = file.readline()
