import matplotlib.pyplot as plt

def diagram(iteration_numbers, fitness_numbers, photo_number):

    fig, ax = plt.subplots()
    func,  = plt.plot(iteration_numbers, fitness_numbers)

    ax.set_title(f"Artificial Bee Colony Algorithm")
    ax.set_xlabel("iteration")
    ax.set_ylabel("fitness")
    name = f"diagram_{photo_number}" + '.png'

    plt.savefig(name)
    plt.show()