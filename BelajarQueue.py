from collections import deque

antrian = deque()

# Customer datang
antrian.append("Ali")
antrian.append("Budi")
antrian.append("Citra")

print("Antrian saat ini:", list(antrian))

# CS melayani customer pertama
customer = antrian.popleft()
print(f"Sedang melayani: {customer}")

print("Antrian sekarang:", list(antrian))
