def first():
    print(type(2 ** 0.5).__name__)

def second():
    harry_spells = 6
    hermiona_spells = 6 * 2
    rhon_spells = hermiona_spells / 4
    print(int((harry_spells + hermiona_spells + rhon_spells) / 3))

def third():
    client = "John Smith"
    first_deposit = 350000
    deposit_after_year = 376250
    print(
f"""Client name: {client}
initial deposit amount: {first_deposit} $
Interest rate: {(deposit_after_year / first_deposit) * 100 - 100:.2f} % per annum and total deposit amount: {deposit_after_year} $ 
""")

first()
second()
third()