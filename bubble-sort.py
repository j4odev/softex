lista = [26,13,23,42,11,69,32,51,9,94]

def bubble_sort(lista):
    for num in range(len(lista)-1,0,-1):
      print(f"primeiro elemento 'segurado' {num}") 
      for i in range(num):
        print(f"segundo elemento 'percorrendo' {i}")
        if lista[i]>lista[i+1]:
            var_temp = lista[i]  
            lista[i] = lista[i+1]
            lista[i+1] = var_temp 
                        
bubble_sort(lista) 
