## 모듈

모듈은 하나의 파이썬 파일을 가르킨다. 이런 모듈안에는 class, function, variable and exectuable code 등이 들어가게 된다.

하나의 파이썬 파일이기 때문에 `my_math.py`와 같은 형식이 된다.
이런 모듈을 쓰기 위해서는 아래 코드와 같이 `import`를 써야 한다.

```python
import my_math
my_math.add(1,2)
```

이런 형식으로 import 할 수 있다.

## 패키지
패키지의 경우 결국 모듈의 합이라고 할 수 있다. 여러가지 module을 합해 둔것이 package이다.
이를 위해서 python에서는 `__init__.py`라는 파이썬 파일을 폴더 내부에 두게 된다. 
이는 파이썬에서 이 폴더가 패키지라고 표시하는 방법이다.

```python
from my_module import my_math
my_math.add(123,123) # 246
```

위와 같이 `from 패키지 import 모듈`형식을 사용해서 모듈을 import할 수 있다.

그렇기 때문에 그동안 [[Dataframe]]을 가지고 놀 때 아래와 같이 `panda` 패키지를 가지고 와서 쓴다는 뜻이다.
```python
import pandas as pd # 판다스 패키지를 가지고 온다. pd라는 이름으로 라는 뜻이다. 
```