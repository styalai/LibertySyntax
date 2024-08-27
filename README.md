# LibertySyntax
How to code without syntax. No syntax, no keywords, and no specific signs, just logistics and LLM.

## Installation as a library
Install it.
```python
pip install git+https://github.com/styalai/LibertySyntax
```
Use it.
```python
from LibertySyntax.libertysyntax import traduce, download_model

model = download_model() # download the model (huggingface pipeline)
code_to_traduce = """
x <- 3
display x + 5
x -> x-2 if x superior 0
print x
"""
code = traduce(model, code_to_traduce)
exec(code)
```

## Installation as a CLI
Install it.
```python
git clone https://github.com/styalai/LibertySyntax
pip install git+https://github.com/styalai/LibertySyntax
cd LibertySyntax
pip install -r requirements.txt
```
Use it.
```python
python libertysyntax.py -file_name file_name.txt
                        -token your_hf_token
                        -stream True
                        -device cpu
                        -model_name model_name_hf
```




