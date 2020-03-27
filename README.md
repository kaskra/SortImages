## **Requirements**
- python 3.8
    - pipenv (pip install pipenv)

## **Installation**
----
```bash
mkdir SortImages-git # Or any other directory name
git clone https://github.com/kaskra/SortImages.git  
cd SortImages-git
pipenv install # Installs the pip environment specifiec in the Pipfile
pipenv run python -m pytest # Test your installation by running the tests
```

## **Execute**
----
Run the program by executing the `run.py` script with following arguments:
```
usage: run.py [-h] -i INPUT -o OUTPUT -e EXTS [EXTS ...]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        an input path to a directory
  -o OUTPUT, --output OUTPUT
                        an output path to a directory
  -e EXTS [EXTS ...], --exts EXTS [EXTS ...]
                        a list of extensions to work on
```
### Example
```bash
pipenv run python .\run.py -e jpg mp4 .PNG -i tests/data -o outputs
```