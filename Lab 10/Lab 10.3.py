import matplotlib.pyplot as plt

vowels = "aAeEiIoOuUyY"

with open("голосні букавкі.txt", "r", encoding="utf-8") as f:
    text = f.read()

freq = {}
for ch in text:
    if ch in vowels:
        freq[ch.lower()] = freq.get(ch.lower(), 0) + 1

letters = sorted(freq.keys())
counts = [freq[l] for l in letters]

plt.figure(figsize=(8, 5))
plt.bar(letters, counts)
plt.xlabel("Голосні літери")
plt.ylabel("Частота появи")
plt.title("Гістограма частоти появи голосних у тексті")
plt.grid(axis="y")

plt.savefig("голосні букавкі.png")
plt.close()