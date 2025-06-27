# Note

Tested by AkagawaTsurunaki.

## New Version

### Environment:
- OS: Ubuntu 24.10
- GPU: NVIDIA GeForce RTX 4090 * 2 (avg 75% used per card)
- Memory: 184 GiB (avg 6.3% used)
- Python: 3.10

Suppose you have Anaconda installed. 
Then you can use `enviroment.yml` to setup your Anaconda environment.

```
conda env update --name dreamer --file environment.yml
```

Activate your environment and check if your GPU devices are available.

```
conda activate dreamer
python test_gpu_available.py
```

## Old version

> [!CAUTION]
>
> The old version of Dreamer may cause `Segmentation fault` or even crash your OS!

If you want to reproduce Dreamer based on the old version of this repo, please checkout the `old` branch.

To setup the enviroment, run the following commands:

```
conda create --name dreamer python=3.8 --yes
conda activate dreamer
pip install -r requirements.txt
conda install cudatoolkit=10.1 cudnn
```

## Contact with Me

**Email:** AkagawaTsurunaki@outlook.com