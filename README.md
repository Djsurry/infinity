# infinity

## Allows for easy use of infinity when using python

> Every wanted to define a variable and then check if its smaller than something, setting it on the first one no matter what? I have and I have always just used something like -1, but that seems crude

## Installation

`python3 -m pip install --index-url https://test.pypi.org/simple/ infinity`

## Usage

```python
from infinity import Infinity
inf = Infinity()
print(inf > 9999999999999999) # True
print(inf < Infinity()) # False
print(inf >= Infinity()) # True

neg_inf = Infinity(negative=True)
print(inf < -9999999999999999) # True
print(inf < Infinity()) # True
print(inf >= Infinity(negative=True)) # True
```
`Infinity` takes in one kwarg, `negative` which defaults to `False`. This indicates weather it should represent negative infinity or positive infinity


