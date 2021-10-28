def is_constant(s):
    return s.lstrip("-").isdigit()


def simple_assembler(program):
    instructions = [i.strip() for i in program]

    index = 0
    register = {}
    while index < len(instructions):
        p = instructions[index].split(' ')
        instruction = p[0]

        if instruction == 'mov':
            x = p[1]
            y = (int(p[2]) if is_constant(p[2]) else register[p[2]])
            register[x] = y
            index += 1
        elif instruction == 'inc':
            x = p[1]
            register[x] = register[x] + 1
            index += 1
        elif instruction == 'dec':
            x = p[1]
            register[x] = register[p[1]] - 1
            index += 1
        elif instruction == 'jnz':
            x = int(p[1]) if is_constant(p[1]) else register[p[1]]
            y = int(p[2]) if x != 0 else 1  # go to the next instruction if x == zero
            index += y
    return register


def test_codewars():
    code = '''\
    mov a 5
    inc a
    dec a
    dec a
    jnz a -1
    inc a'''
    assert simple_assembler(code.split('\n')) == {'a': 1}

    code = '''\
    mov c 12
    mov b 0
    mov a 200
    dec a
    inc b
    jnz a -2
    dec c
    mov a b
    jnz c -5
    jnz 0 1
    mov c a'''
    assert simple_assembler(code.split('\n')) == {'a': 409600, 'c': 409600, 'b': 409600}


def test_failing():
    program = ['mov a -10', 'mov b a', 'inc a', 'dec b', 'jnz a -2']
    assert simple_assembler(program) == {'a': 0, 'b': -20}
