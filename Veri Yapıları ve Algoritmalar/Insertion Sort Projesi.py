# Insertion Sort Projesi

# [22,27,16,2,18,6] -> Insertion Sort
# Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.

def insertion_sort_with_steps(arr): # Insertion Sort algoritmasını kullanarak diziyi sıralar ve her adımı yazdırır.
    
    print(f"Başlangıç Durumu: {arr}")
    # Dizinin ilk elemanı zaten sıralı kabul edilir.
    # Bu yüzden ikinci elemandan (index 1) başlar.
    for i in range(1, len(arr)):
        key = arr[i]  # Sıralanacak olan eleman
        j = i - 1

        # 'key' elemanını, ondan büyük olan tüm elemanların sağına taşı.
        # Bu döngü, 'key' için doğru konumu bulana kadar devam eder.
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # 'key' elemanını doğru konumuna yerleştir.
        arr[j + 1] = key
        print(f"Adım {i}: {arr}")
    
    print(f"Sıralanmış Hali: {arr}")

# Sıralanacak dizi
dizi = [22, 27, 16, 2, 18, 6]
insertion_sort_with_steps(dizi)

# Big-O gösterimini yazınız.
# Worst Case (En Kötü Durum): O(n^2) - Dizi ters sırada olduğunda. Her eleman için dizinin sıralı kısmı kadar karşılaştırma ve kaydırma gerekir.
# Average Case (Ortalama Durum): O(n^2) - Elemanlar rastgele dağıldığında.
# Best Case (En İyi Durum): O(n) - Dizi zaten sıralı olduğunda. Her eleman sadece bir önceki elemanla karşılaştırılır.

# Time Complexity: Dizi sıralandıktan sonra 18 sayısı aşağıdaki case'lerden hangisinin kapsamına girer? 
# Dizi sıralandıktan sonra: [2, 6, 16, 18, 22, 27]
# 18 sayısının konumu: Ortada (index 3)
# 18 sayısı "Average Case" kapsamına girer.