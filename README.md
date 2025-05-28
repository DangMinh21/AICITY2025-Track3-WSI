# AI City Challenge 2025
## Track 3: Warehouse Spatial Intelligence

* Go to challenge: [Click here](https://www.aicitychallenge.org/2025-track3/)

```shell
# Propose project structure
AICITY2025-Track3-WSI/
├── .git/                     # Git repository files (hidden)
├── .vscode/                  # VSCode workspace settings (e.g., interpreter path)
│   └── settings.json
├── data/
│   ├── raw/                  # Raw dataset files (or symlinks/pointers to them)
│   │   └── PhysicalAI-Spatial-Intelligence-Warehouse/ # Link to Hugging Face dataset
│   ├── processed/            # Processed data (e.g., pre-computed features, specific formats)
│   └── dataset_info.md       # Notes about the dataset, download links, etc.
│
├── notebooks/                # Jupyter notebooks for exploration, visualization, quick tests
│   ├── 01_data_exploration.ipynb
│   └── 02_model_prototyping.ipynb
│
├── src/                      # Main source code
│   ├── __init__.py
│   ├── data_processing/      # Scripts for data loading, preprocessing, augmentation
│   │   ├── __init__.py
│   │   ├── loader.py         # Dataset class(es)
│   │   └── preprocess.py     # Preprocessing functions
│   ├── models/               # 3D-VLM model definitions, wrappers, or specific components
│   │   ├── __init__.py
│   │   └── your_3dvlm.py     # Your model architecture or interface to a pre-trained one
│   ├── engine/               # Training, evaluation, and inference pipelines/loops
│   │   ├── __init__.py
│   │   ├── train.py
│   │   ├── evaluate.py
│   │   └── infer.py
│   ├── utils/                # Utility functions (logging, metrics, helpers)
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   └── metrics.py
│   └── main.py               # Main script to orchestrate training/evaluation (optional)
│
├── configs/                  # Configuration files (e.g., hyperparameters, model settings)
│   ├── base_config.yaml
│   └── experiment_001.yaml
│
├── scripts/                  # Shell scripts for running common tasks
│   ├── train_model.sh
│   ├── evaluate_model.sh
│   └── download_dataset.sh   # Script to download/setup dataset (optional)
│
├── outputs/                  # Output files from training and experiments
│   ├── experiments/
│   │   └── experiment_001/
│   │       ├── checkpoints/    # Saved model checkpoints
│   │       ├── logs/           # Training logs
│   │       └── predictions/    # Generated predictions (predictions.json)
│   ├── visualizations/       # Any saved plots or visualizations
│
├── .gitignore                # Specifies intentionally untracked files that Git should ignore
├── README.md                 # Project overview, setup instructions, how to run
├── environment.yml           # Conda environment specification (export with `conda env export > environment.yml`)
└── requirements.txt          # Alternative for pip: (generate with `pip freeze > requirements.txt`)
```
## Notes
* Download data run: notebooks/download_dataset.ipynb 