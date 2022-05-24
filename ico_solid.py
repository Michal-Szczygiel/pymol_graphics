from pymol import cgo
import random

vertices = []
vert_faces = []
normals = []
norm_faces = []

#color = lambda: [0, random.uniform(120 / 255, 170 / 255), random.uniform(210 / 255, 1)]
color = lambda: [180 / 255, 255 / 255, 76 / 255]

with open('ico.obj') as obj_file:
    for line in obj_file:
        data = line.split()

        if len(data) == 0:
            continue

        if data[0] == 'v':
            vertices.append([float(data[1]), float(data[2]), float(data[3])])

        if data[0] == 'vn':
            normals.append([float(data[1]), float(data[2]), float(data[3])])

        if data[0] == 'f':
            x_coords = data[1].split('/')
            y_coords = data[2].split('/')
            z_coords = data[3].split('/')

            vert_faces.append([
                int(x_coords[0]) - 1,
                int(y_coords[0]) - 1,
                int(z_coords[0]) - 1
            ])

            norm_faces.append([
                int(x_coords[2]) - 1,
                int(y_coords[2]) - 1,
                int(z_coords[2]) - 1
            ])


shape = [cgo.BEGIN, cgo.TRIANGLES]

for vert_face, norm_face in zip(vert_faces, norm_faces):
    shape += [
        cgo.VERTEX, *vertices[vert_face[0]], cgo.NORMAL, *normals[norm_face[0]], cgo.COLOR, *color(),
        cgo.VERTEX, *vertices[vert_face[1]], cgo.NORMAL, *normals[norm_face[1]], cgo.COLOR, *color(),
        cgo.VERTEX, *vertices[vert_face[2]], cgo.NORMAL, *normals[norm_face[2]], cgo.COLOR, *color()
    ]

shape.append(cgo.END)

cmd.load_cgo(shape, 'ico_solid')
