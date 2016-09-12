MAX_VALUE = 99999999

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

    if 'edgeWeightType: ' in line:
        (aux, weightType) = line.split(" ")
        weightType = weightType.replace('\n', '').replace('\r', '')
        tipo = weightType
        print(tipo)

    line = file.readline()

# Criação da matriz de adjacência
Matrix = [0 for x in range(num_Nodes)]
for x in range(num_Nodes):
    line = file.readline()
    line = line.split(" ", num_Nodes)
    del line[num_Nodes]
    Matrix[x] = line

# Definição do elemento nulo da matriz (elemento da diagonal principal)
NullElement = int(Matrix[0][0])


# Leitura do resto do arquivo
line = file.readline()
while line:
    # Criação do vetor de demanda
    if 'Demand' in line:
        line = file.readline()
        line = line.split(" ",num_Nodes)
        del line[num_Nodes]
        Demand = line

    # Criação do vetor de calado
    if 'Draft' in line:
        line = file.readline()
        line = line.split(" ", num_Nodes)
        del line[num_Nodes]
        Draft = line

    line = file.readline()

Load = 0
for x in Demand:
    Load += int(x)

CandidateValue = MAX_VALUE   #Inicia em um valor alto
CandidateIndex = 0
VisitedPorts = [1]
'''
x = 0
while Load != 0:
    for y in range(num_Nodes):
        if (int(Matrix[x][y]) < CandidateValue) & (int(Matrix[x][y]) != NullElement):    #tratamento do custo
            if ((y+1) not in VisitedPorts) & (Load <= int(Draft[y])):   #tratamento dos portos já visitados e do calado
                CandidateValue = int(Matrix[x][y])
                CandidateIndex = y

    TotalCost += CandidateValue
    CandidateValue = MAX_VALUE
    VisitedPorts.append(CandidateIndex+1)
    Load -= int(Demand[y])
    x = CandidateIndex

    if Load == 0:
        VisitedPorts.append(1)
        TotalCost += int(Matrix[x][0])


print ('TotalCost = ', TotalCost)
print ('VisitedPorts = ', VisitedPorts)
print ('Load = ', Load)
'''