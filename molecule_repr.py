from pymol import cgo

COLORS = {
    'N': [1, 0, 0],
    'H': [1, 1, 1],
    'C': [0.25, 0.25, 0.25],
    'O': [0, 0, 1],
    'S': [0.75, 0.25, 0.12]
}

atoms = []

with open('6kbh.pdb') as pdb_file:
    for line in pdb_file:
        data = line.split()

        if data[0] == 'ATOM':
            atoms.append((float(data[6]), float(data[7]), float(data[8]), data[2][0]))


spheres = []

for atom in atoms:
    color = None

    try:
        color = COLORS[atom[3]]
    except:
        color = [0, 1, 0]

    spheres += [cgo.COLOR, *color, cgo.SPHERE, *atom[:3], 0.5]


cmd.load_cgo(spheres, 'molecule_repr')
