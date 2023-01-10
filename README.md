# python_multidimensional_list_search

You can search any items from multidimensional list, tuple, or ndarray in Python.

Pythonの多次元リスト（またはタプル, ndarray）について、任意の要素が含まれているかを検索するための関数を作りました。

## QuickAPI

If you want to search from 2-dimensional list, you can use this quick API.

2次元配列から要素の検索を行いたい場合は、以下のクイックAPIを使うことで検索が可能です。

```python
import numpy as np

from typing import Union

def two_dim_search(
                     input_list:Union[tuple,list,np.ndarray],
                     query:Union[tuple,list,np.ndarray],
                     contains_all=False
                  ):

     if contains_all:
         return [i for i,l in enumerate(input_list) if all(map(lambda x:x in l, query))]
     else:
         return [i for i,l in enumerate(input_list) if any(map(lambda x:x in l, query))]
```

### QuickAPI sample

```python
# 不規則次元を含まない2次元配列のみ入力可能
list1 = [[1,2,3],[2,3,4],[3,4,5]]
string_list1 = [["aaa","bbb","ccc"],["aaa","bbb","ccc"],["aaa","bbb","ccc"]]

# 1,2および"aaa","bbb","ccc"を含むかどうか調べる
query = [1,2]
string_query = ["aaa","bbb","ccc"]
```

```python
# [1,2]のどちらか一方でも入っているか調べる例
print(two_dim_search(list1, query, contains_all=False))  # [0, 1]

# [1,2]の全てが入っているか調べる例
print(two_dim_search(list1, query, contains_all=True))  # [0]

# "aaa","bbb","ccc"のいずれか一つでも入っているか調べる例
print(two_dim_search(string_list1, string_query, contains_all=False))  # [0, 1, 2]

# "aaa","bbb","ccc"の全てが入っているか調べる例
print(two_dim_search(string_list1, string_query, contains_all=True))  # [0, 1, 2]
```

## How to use

You can use a function `multidemantion_search()` in `multidimension_search.py` or try jupyter notebook `codes.ipynb` for tutorial.

`multidimension_search.py`内の`multidemantion_search()`関数を使って多次元リストの検索が行えるほか、コードサンプル/チュートリアルとして`codes.ipynb`をjupyter notebookとして用意しています。

## Detail informations

You can read more detail informations about this repo on at [<b>my blog</b>](https://www.tsukutarou.net/entry/python_multidimensional_list_search).

実装に関する詳しい説明など、[<b>私のブログ</b>](https://www.tsukutarou.net/entry/python_multidimensional_list_search)で紹介しています。

<iframe src="https://hatenablog-parts.com/embed?url=https%3A%2F%2Fwww.tsukutarou.net%2Fentry%2Fpython_multidimensional_list_search" title="【Python】2次元・3次元・多次元リスト(list)内に任意の要素があるか検索 - つくたろうのブログ" class="embed-card embed-blogcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 190px; max-width: 500px; margin: 10px 0px;" loading="lazy"></iframe>

***

## Author

<b>Tsukutarou / つくたろう</b>

GitHub: <a href="https://github.com/tsukutarou">tsukutarou</a>

Email: email[at]tsukutarou.net

Blog: <a href="https://www.tsukutarou.net">https://www.tsukutarou.net</a> 