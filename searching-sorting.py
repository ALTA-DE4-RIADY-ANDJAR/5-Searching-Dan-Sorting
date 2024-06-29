
#Problem 1

numbers = [5, 7, 4, -2, -1, 8]
min_value = min(numbers)
min_index = numbers.index(min_value)

max_value = max(numbers)
max_index = numbers.index(max_value)

print(f'Nilai minimum: {min_value} pada indeks {min_index}')
print(f'Nilai maksimum: {max_value} pada indeks {max_index}')




#Prblem 2

def max_buy_products(money, prices):
    # Inisialisasi variabel untuk melacak total yang telah dibelanjakan
    total_spent = 0
    # List untuk menyimpan barang yang telah dibeli
    barang_dibeli = []
    # Set untuk menyimpan barang yang sudah dibeli agar tidak membeli barang yang sama lagi
    sudah_dibeli = set()

    # Mengurutkan harga produk dari terendah ke tertinggi
    sorted_prices = sorted(prices)

    # Iterasi untuk membeli barang
    for price in sorted_prices:
        if total_spent + price <= money and price not in sudah_dibeli:
            barang_dibeli.append(price)
            sudah_dibeli.add(price)
            total_spent += price

    return barang_dibeli


money = 50000
prices = [25000, 25000, 10000, 14000]

barang_dibeli = max_buy_products(money, prices)

print(f"Jumlah barang yang berhasil dibeli: {len(barang_dibeli)}")




#Problem 4
items = ["js", "js", "golang", "ruby", "ruby", "js", "js"]

def count_item_sort(items):
    item_count = {}
    
    # Menghitung kemunculan setiap barang
    for item in items:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1
    
    # Mengurutkan barang berdasarkan jumlah kemunculannya (descending)
    sorted_items = sorted(item_count.items(), key=lambda x: x[1], reverse=False)
    

    print("Barang dengan jumlah kemunculan tertinggi:")
    seen_items = set()
    for item, count in sorted_items:
        if item not in seen_items:
            print(f"{item}: {count} kali")
            seen_items.add(item)

count_item_sort(items)

