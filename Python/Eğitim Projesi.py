#Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden oluşabileceği gibi, non-scalar verilerden de oluşabilir.
def flatten_list(nested_list):
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))  
        else:
            flat.append(item)
    return flat

input1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output1 = flatten_list(input1)
print(output1) # Çıktı: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]

#Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.
def reverse_nested_list(lst):
    reversed_list = []
    for item in reversed(lst):
        if isinstance(item, list):
            reversed_list.append(reverse_nested_list(item))  
        else:
            reversed_list.append(item)
    return reversed_list

input2 = [[1, 2], [3, 4], [5, 6, 7]]
output2 = reverse_nested_list(input2)
print(output2) # Çıktı: [[7, 6, 5], [4, 3], [2, 1]]