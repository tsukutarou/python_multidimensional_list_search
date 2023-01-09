import collections
import numpy as np

from typing import Union


# リストのネストの深さを求める関数
def nest_depth(item:Union[tuple,list,np.ndarray]):

     if not item:
         return 0
     else:
         if isinstance(item, (tuple,list,np.ndarray)):
             return max([nest_depth(i) for i in item]) + 1
         else:
             return 0


# リストを決められた回数だけ平坦化する関数
def flatten(input_list, flatten_num:int):

     flatten_num = flatten_num - 1

     if flatten_num < 0:
         for item in input_list:
             yield item
     else:
         for item in input_list:
             if isinstance(item, collections.abc.Iterable) and not isinstance(item, (str, bytes)):
                 yield from flatten(item, flatten_num)
             else:
                 yield item


# 不規則な次元を含んだ多次元リストかどうかをチェックする関数
def isirregular(input_list):
     
     flatten_num = nest_depth(input_list) - 2

     flattened_list = list(flatten(input_list, flatten_num))

     return not len(list(set([nest_depth(item) for item in flattened_list]))) == 1