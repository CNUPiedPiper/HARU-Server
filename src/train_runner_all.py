import sys
from trainer import trainer
import os.path

# If you add a new function, use the follwing module to update the feature value which stored in model directory.
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(os.path.dirname(__file__))
        print '$python trainer.py model_number iteration_number'
        exit()

    for i in range(1, int(sys.argv[1]) + 1):
        os.system(''.join(['python train_runner.py ', str(i), ' ', sys.argv[2]]))