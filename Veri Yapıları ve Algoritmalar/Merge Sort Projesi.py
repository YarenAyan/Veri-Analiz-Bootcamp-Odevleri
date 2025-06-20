# Merge Sort Projesi 

# [16,21,11,8,12,22] -> Merge Sort
# Yukarıdaki dizinin sort türüne göre aşamalarını yazınız.

def merge_sort_with_steps(arr): # Verilen listeyi Merge Sort algoritması ile sıralar ve adımları gösterir.

    if len(arr) > 1:
        print(f"Bölünüyor: {arr}")
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Özyinelemeli olarak her iki yarıyı da sırala.
        merge_sort_with_steps(left_half)
        merge_sort_with_steps(right_half)

        # Geçici dizilerdeki verileri birleştir.
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Kalan elemanları ekle.
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        
        print(f"Birleştiriliyor: {arr}")

# Sıralanacak dizi
dizi = [16, 21, 11, 8, 12, 22]
print(f"Başlangıç Dizisi: {dizi}")

merge_sort_with_steps(dizi)
print(f"Sıralanmış Dizi: {dizi}")

# Big-O gösterimini yazınız.

# Time Complexity (Zaman Karmaşıklığı): O(n log n)
# Merge Sort'un zaman karmaşıklığı en kötü, ortalama ve en iyi durumda da O(n log n)'dir.
# Bunun nedeni, dizinin her seferinde ikiye bölünmesi (log n) ve her birleştirme adımının dizideki tüm elemanları (n) gezmesidir.

# Space Complexity (Alan Karmaşıklığı): O(n)
# Birleştirme işlemi sırasında sol ve sağ yarıları tutmak için geçici diziler oluşturulur.
# Bu geçici dizilerin boyutu orijinal dizinin boyutu (n) kadardır.