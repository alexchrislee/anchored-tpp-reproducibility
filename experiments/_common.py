"""Shared setup for experiment scripts."""
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

plt.rcParams.update({"font.size": 9, "axes.titlesize": 10, "axes.labelsize": 9,
                     "axes.grid": True, "grid.alpha": 0.3, "figure.dpi": 150,
                     # Springer production rejects Type 3 fonts.  Matplotlib
                     # emits Type 3 by default; 42 selects embedded TrueType.
                     "pdf.fonttype": 42, "ps.fonttype": 42})

FIGDIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                      "figures")
os.makedirs(FIGDIR, exist_ok=True)


def save(fig, name):
    path = os.path.join(FIGDIR, name)
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"  wrote figures/{name}")
    return path
