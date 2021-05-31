# UAGenerater (Deprecated)
### A Fast User Agent Generater in Python.

## Independence
### Python
Python 3.5 is tested, and 3.5 is the most recommended version, also Python 2 is supported.

## Usage
### Basic Usage
```python
import  UAGenerater as uag
ua = uag.uasingle()
print(ua)
```
##### <em>The User Agent returned is a <strong>string</strong> type.</em>

### Advance Usage
```python
import  UAGenerater as uag
f = open('user-agent.txt', 'w+')
f.write(str(uag.ualist(1000)))
f.close()
```
##### <em>The User Agent saved is a <strong>list</strong> type.</em>
