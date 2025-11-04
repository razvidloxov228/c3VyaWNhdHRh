books = {
    "1984": 1949,
    "Пригоди Шерлока Холмса": 1892
}
books["Linux From Scratch"] = 1999
print("Мої улюблені книги:")
for title, year in books.items():
    print(f"«{title}» — {year}")
