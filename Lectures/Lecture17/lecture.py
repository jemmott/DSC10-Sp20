from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


def sampling_animation(population):
    fig = plt.figure();
    plt.xlim([61_000, 73_000])
    ax = plt.gca()
    ax.set_yticklabels([]);

    scatter = plt.scatter([], [], alpha=.5, marker='x', s=80)
    title = plt.title('')

    sizes = [1, 2, 3, 4, 8, 16, 32, 64, 128]
    medians = []
    np.random.seed(4242)
    for _ in range(sizes[-1]):
        s = population.sample(500, replace=True)
        m = np.median(s.get('Total Pay'))
        medians.append(m)

    def animate(i):
        n_samples = sizes[i]
        subset = medians[:n_samples] 
        scatter.set_offsets(np.column_stack([subset, np.zeros_like(subset)]))
        title.set_text(f'n_samples = {sizes[i]}')
    
    anim = FuncAnimation(fig, animate, frames=len(sizes), interval=500)
    return anim, medians
