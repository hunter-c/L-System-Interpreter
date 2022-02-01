import turtle
import random

# http://algorithmicbotany.org/papers/abop/abop-ch1.pdf

# L-system rules from http://paulbourke.net/fractals/lsys/

def iterate(axiom, rules, num_iterations=3):
    constants = ['+', '-', '[', ']', '>']

    # creates new iteration by replacing current iters symbols based on rules
    def new_iteration(current):
        iteration = '' # clear old rules to build new iteration
        for char in current:
            if char in constants:
                iteration += char
            else:
                iteration += rules.get(char, '')
        return iteration

    iteration = axiom
    for i in range(num_iterations):
        iteration = new_iteration(iteration)
        print(f"Iteration: {i + 1} \n {iteration}")
    return iteration

def draw(iteration, distance=10, angle=30, length_factor=1):
    stack = []
    cursor = turtle.Turtle()
    #cursor.hideturtle()
    # turtle.tracer(0, 0)
    cursor.speed(0)
    cursor.left(90)
    cursor.left(90)

    turtle.setup(width = 1700, height = 900, startx = None, starty = None)


    for op in iteration:
        if op == "F":
            cursor.forward(distance)
        elif op == "+":
            cursor.right(angle)
        elif op == "-":
            cursor.left(angle)
        elif op == "[":
            stack.append((cursor.heading(), cursor.position()))
        elif op == "]":
            heading, position = stack.pop()
            cursor.penup()
            cursor.goto(position)
            cursor.setheading(heading)
            cursor.pendown()
        elif op == ">":
            distance = distance * length_factor
        elif op == "<":
            distance = int(distance / length_factor)
    #turtle.update()

def generate_system():
    angles = [15, 30, 45, 60, 70, 90, 120, 135, 270]
    constants = ['F', '+', '-', '[', ']', '>', '<']
    
    two_rule = bool(random.randrange(2))
    # if random.randrange(10) % 2 == 0:
    #     pass

    axiom = ""
    rule = ""
    size = random.randrange(4, 10)

    # for i in range(size // 2):
    #     axiom += 


    # for i in range(rule_size):


def main():

    # draw(iterate("F", {"F": "F[-F][+F]"}, 5), 20, 30 ) # Tree
    # draw(iterate("F", {"F": "FF+[+F-F-F]-[-F+F+F]"}), 10, 15) # Seaweed
    # draw(iterate("X", {"F": "FF", "X": "F[+X]F[-X]+X"}, 5), 5, 20) # Sticks
    # draw(iterate("F+F+F+F", {"F": "FF+F-F+F+FF"}), 10, 90) # Maze thing
    # draw(iterate("F", {"F": "F[+FF][-FF]F[-F][+F]F"}), 10) # plant
    # draw(iterate("FX", {"F": "F","X": ">[-FX]+FX"}, 5), 20, 40, .95) # incomplete
    # draw(iterate("F+F+F", {"F": "F-F+F"}, 8), 10, 120) # triangular grid
    # draw(iterate("F", {"F":"-F++F-"}, 10), 10, 45) # Levy curve
    # draw(iterate("F", {"F":"+FF--FF+"}, 6), 15, 120) # custom
    # draw(iterate("FXF", {"F":"+FF+", "X":"FF"}, 10), 30, 30) # Lotus of sorts
    # draw(iterate("FXF", {"F":"+FXF+", "X":"FF"}, 7), 30, 30) # geometric lotus shape
    # draw(iterate("YF", { "G":"F+G+F"}, 10), 10, 60) # sierpinsky triangle
    # draw(iterate("YF", {"F":"F", "X":"YF+XF+Y", "Y":"XF-YF-X"}, 3), 10, 60) # sierpinsky triangle
    # draw(iterate("a", {"F": ">F<", "a": "F[+x]Fb", "b": "F[-y]Fa", "x": "a", "y": "b"}, 9), 1, 45, 1.2) # leaf sort of
    draw(iterate("a", {"F": "+F[a]F+F[a]F---FaF+FaF+", "a": "-FFF-"}, 5), 3, 12) # leaf sort of

    # irritating... well, heh... ehm, just an annoying continuation of the last few monthes, of which, I have had the unfortunate opportunity of experiencing in their entirety.

    turtle.done()

if __name__ == "__main__":
    main()