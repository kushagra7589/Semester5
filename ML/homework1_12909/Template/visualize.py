import os
import os.path
import argparse
from sklearn.manifold import TSNE

parser = argparse.ArgumentParser()
parser.add_argument("--data", type = str  )
parser.add_argument("--plots_save_dir", type = str  )

args = parser.parse_args()
