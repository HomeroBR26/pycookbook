def length(sizes, goal):
    remainders = []
    containers = []
    container = []
    fill = goal

    for size in sizes:
        qty = min(fill // size[0], size[1])
        fill = fill - (qty * size[0])
        remainders.append((size[0], size[1] - qty))
        container.append((size[0], qty))

    if any([size[1] for size in sizes]):
        containers = length(remainders, goal)
    else:
        return containers

    containers.append((container, fill))
    return containers

if __name__ == '__main__':
    sizes = [
        (85.75, 10),
        (65, 4),
        (38, 4),
        (12, 2),
        (8, 2)
    ]
    dist = list(reversed(length(sorted(sizes, reverse=True), 156)))

    for elem in dist:
        print("Distribución de Cortes: {}  ||  Espacio restante en contenedor: {}".format(elem[0], elem[1]))