# LibertySyntax
How to code without syntax. No syntax, no keywords, and no specific signs, just logistics and LLM.

# Installation as a library
```python
pip install git+https://github.com/styalai/LibertySyntax
```
How to use it.
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
