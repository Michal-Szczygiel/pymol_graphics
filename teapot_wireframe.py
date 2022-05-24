from pymol import cgo

vertices = []
vert_faces = []

with open('teapot_norm.obj') as obj_file:
    for line in obj_file:
        data = line.split()

        if len(data) == 0:
            continue

        if data[0] == 'v':
            vertices.append([float(data[1]), float(data[2]), float(data[3])])

        if data[0] == 'f':
            vert_faces.append([])

            for element in data[1:]:
                vert_faces[-1].append(int(element.split('/')[0]) - 1)


shape = [cgo.BEGIN, cgo.LINES]

for vert_face in vert_faces:
    for i in range(len(vert_face)):
        if i + 1 < len(vert_face):
            shape += [
                cgo.VERTEX, *vertices[vert_face[i]],
                cgo.VERTEX, *vertices[vert_face[i + 1]]
            ]
        else:
            shape += [
                cgo.VERTEX, *vertices[vert_face[i]],
                cgo.VERTEX, *vertices[vert_face[0]]
            ]


shape.append(cgo.END)

cmd.load_cgo(shape, 'teapot_wireframe')
