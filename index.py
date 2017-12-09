print ("######################")
print ("######Calculadora#####")
print ("#######Jeancode#######")
print ("######################")

while 1:
    print("Elige una opcion opcion")
    print("->Suma(1)")
    print("->Resta(2)")
    print("->multiplicacion(3)")
    print("->divicion(4)")
    entrada =  raw_input("->")

    if entrada == "1":
        print "sumando"
        n1 = input("Primer Numero:")
        n2 =input("Segundo Numero:")
        print "Resutado:"n1 + n2
        raw_input("")
        

    if entrada == "2":
        print "Restando"
        n1 =  input("Primer Numero:")
        n2 =  input("Segundo Numero:")
        print n1 - n2
        raw_input("")
        
    if entrada == "3":
        print "Multiplicando"
        n1 =  input("Primer Numero:")
        n2 =  input("Segundo Numero:")
        print n1 * n2
        raw_input("")
        
    if entrada == "4":
        print "Dividiendo"
        n1 = input("Primer Numero:")
        n2 =  input("Segundo Numero:")
        print n1 / n2
        raw_input("");
    


    
