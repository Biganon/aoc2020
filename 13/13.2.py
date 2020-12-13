from sympy.ntheory.modular import crt

lines = ((13, 0), (41, 3), (37, 7), (659, 13), (19, 32), (23, 36), (29, 42), (409, 44), (17, 61))

moduli = [x[0] for x in lines]
residues = [x[1] for x in lines]

a, b = crt(moduli, residues)
print(a, b)
print(b-a)