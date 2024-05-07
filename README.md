# MT Exercise 4: Layer Normalization for Transformer Models

This repo is a collection of scripts showing how to install [JoeyNMT](https://github.com/joeynmt/joeynmt), download
data and train & evaluate models, as well as the necessary data for training your own model

# Requirements

- This only works on a Unix-like system, with bash.
- Python 3.10 must be installed on your system, i.e. the command `python3` must be available
- Make sure virtualenv is installed on your system. To install, e.g.

    `pip install virtualenv`

## Modifications

**Changes to the YAML file for Training Model with Pre-Norm**
To train the model with pre-norm, the following changes were made to the `deen_transformer_regular.yaml` file (renamed as `deen_transformer_prenorm.yaml`):
1. **Model Name:**
   - Changed the `name` field to `"deen_transformer_prenorm"` to indicate that this configuration is for training a model with pre-norm.
2. **Encoder and Decoder Configuration:**
   - Added `layer_norm: "pre"` under both `encoder` and `decoder` sections. This setting specifies that layer normalization should be applied before the sub-layers, implementing pre-norm.
3. **Model Directory:**
   - Changed the `model_dir` field to `"models/deen_transformer_prenorm"` to indicate the directory where the model checkpoints and logs will be saved.

**Changes to the `train.sh` script for Training Model with Pre-Norm (renamed as `train_prenorm.sh`)**
To train the model with pre-norm, the following changes were made to the training script (`train.sh`, which was renamed as `train_prenorm.sh`):
1. **Base:**
   - Replaced `base=$scripts/..` with `base=$(cd "$scripts"/.. && pwd)` to improve compatibility on macOS.
2. **Number of Threads:**
   - The `num_threads` variable is adjusted to `7` according to the number of cores on CPU.
3. **Model Name:**
   - The `model_name` variable is set to `deen_transformer_prenorm`, indicating the pre-norm configuration. This ensures that the correct model directory is used for storing checkpoints and logs for the pre-norm model.
4. **Configuration File:**
   - The configuration file is referenced specific to the pre-norm model (`deen_transformer_prenorm.yaml`). This ensures that the correct configuration is used for training the pre-norm model.
These changes in `train_prenorm.sh` adapt the training script for the pre-norm model, enabling the comparison with the baseline model trained using `train.sh`.

**Changes to the YAML file for Training Model with Post-Norm**
To train the model with post-norm, the following changes were made to the `deen_transformer_regular.yaml` file (renamed as `deen_transformer_postnorm.yaml`):
1. **Model Name:**
   - Changed the `name` field to `"deen_transformer_postnorm"` to indicate that this configuration is for training a model with post-norm.
2. **Encoder and Decoder Configuration:**
   - Added `layer_norm: "post"` under both `encoder` and `decoder` sections. This setting specifies that layer normalization should be applied before the sub-layers, implementing post-norm.
3. **Model Directory:**
   - Changed the `model_dir` field to `"models/deen_transformer_postnorm"` to indicate the directory where the model checkpoints and logs will be saved.

**Changes to the `train.sh` script for Training Model with Post-Norm (renamed as `train_postnorm.sh`)**
To train the model with post-norm, the following changes were made to the training script (`train.sh`, which was renamed as `train_postnorm.sh`):
1. **Base:**
   - Replaced `base=$scripts/..` with `base=$(cd "$scripts"/.. && pwd)` to improve compatibility on macOS.
2. **Number of Threads:**
   - The `num_threads` variable is adjusted to `7` according to the number of cores on CPU.
3. **Model Name:**
   - The `model_name` variable is set to `deen_transformer_postnorm`, indicating the post-norm configuration. This ensures that the correct model directory is used for storing checkpoints and logs for the post-norm model.
4. **Configuration File:**
   - The configuration file is referenced specific to the post-norm model (`deen_transformer_postnorm.yaml`). This ensures that the correct configuration is used for training the post-norm model.
These changes in `train_postnorm.sh` adapt the training script for the post-norm model.

**Addition of `extract_perplexities.py` Script to Extract Perplexities**
1. **Functionality**: This script extracts validation perplexity values from training log files of machine learning models.
2. **Usage**: It reads log files for baseline, pre-norm, and post-norm models, saving the extracted perplexity values into separate CSV files under the 'logs' directory.
3. **Execution**: Simply run the script in your Python environment, ensuring the required log files are available.

**Addition of `create_table.py` Script to Generate Perplexity Tables**
1. **Functionality**: This script combines validation perplexity values extracted from the log files of baseline, pre-norm, and post-norm models into a single CSV table.
2. **Usage**: After extracting perplexities using `extract_perplexities.py`, execute this script to merge the perplexity values and create a comprehensive table.
3. **Output**: The script generates a CSV file named `perplexity_table.csv` in the 'logs' directory, containing validation perplexity values for each model at intervals of 500 steps.

**Addition of `create_line_charts.py` Script to Visualize Perplexity Results**
1. **Functionality**: This script generates a line chart visualizing the validation perplexity results of the baseline, pre-norm, and post-norm models.
2. **Usage**: After creating the perplexity table using `create_table.py`, execute this script to create a line chart showing the progression of perplexity values over validation steps.
3. **Output**: The script generates a line chart named `line_chart.png` in the 'logs' directory, with distinct colors representing each model for easy comparison of model performance.


# Steps

Clone this repository or your fork thereof in the desired place:

    git clone https://github.com/moritz-steiner/mt-exercise-4

Create a new virtualenv that uses Python 3. Please make sure to run this command outside of any virtual Python environment:

    ./scripts/make_virtualenv.sh

**Important**: Then activate the env by executing the `source` command that is output by the shell script above.

Make sure to install the exact software versions specified in the exercise sheet before continuing.

Download Moses for post-processing:

    ./scripts/download_install_packages.sh


Train a model:

    ./scripts/train.sh

The training process can be interrupted at any time, and the best checkpoint will always be saved. It is also possible to continue training from there later on.


Train a model with pre-norm:

    ./scripts/train_prenorm.sh


Train a model with post-norm:

    ./scripts/train_postnorm.sh


Extract perplexities from log files:

    python scripts/extract_perplexities.py


Create a table from csv files:

    python scripts/create_table.py


Create line charts from csv table:

    python scripts/create_line_charts.py
