def value(colors):
    color_code = [
        'black',
        'brown',
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'violet',
        'grey',
        'white'
    ]

    first = color_code.index(colors[0])
    second = color_code.index(colors[1])

    return first * 10 + second
