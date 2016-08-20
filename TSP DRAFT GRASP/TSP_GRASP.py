#def read_file(instance, num, tipo):
	
print("Informe o nome da instancia")
instance = input()
	
file = open(instance, 'r')
print('File opened')

line = file.readline()
	
while ('Distance' not in line):
        
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
            
    print("final")        
    line = file.readline()
    print(line)
    #Coment

