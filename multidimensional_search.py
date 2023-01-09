import numpy as np

from typing import Union
from helper import nest_depth, isirregular


# 多次元のリストから任意の要素について検索してインデックスを調べる関数
"""
入力引数:
     input_list: 要素が存在しているか調べたいリスト(またはタプル, ndarray)
     query: 調べたい要素 (リストやタプルの形で複数渡すことも可能)
     contains_all: queryの全ての要素をもつ要素のインデックスが欲しい場合はTrue.
     デフォルトではFalse (query内のどれか一つでも該当するものを検索)

返り値:
     (不規則次元を持たない場合) 該当する要素番号を持った多次元リスト. ネストの深さが元のリスト準拠.
     (不規則次元を持つ場合) Noneを返却. 標準出力にエラーメッセージ出力.
"""
def multidimension_search(
                             input_list:Union[tuple,list,np.ndarray],
                             query:Union[int,str,tuple,list,np.ndarray],
                             contains_all=False
                         ):
                        
     if isirregular(input_list):
         print("An irregular dimensional list cannot be saerchable.")
         return
     
     if isinstance(query, (int, str)):
         query = [query]

     if nest_depth(input_list) == 1:
         if contains_all:
             return all(map(lambda x:x in input_list, query))
         else:
             return [i for i,l in enumerate(input_list) if any(map(lambda x:x == l, query))]
     elif nest_depth(input_list) > 2:
         return [multidimension_search(sublist,query,contains_all) for sublist in input_list]

     if contains_all:
         return [i for i,l in enumerate(input_list) if all(map(lambda x:x in l, query))]
     else:
         return [i for i,l in enumerate(input_list) if any(map(lambda x:x in l, query))]


# 動作確認用 (codes.ipynbと同じ)
def main():
     list1 = [[1,2,3],[2,3,4],[3,4,5]]
     list2 = [[[11,12,13],[1,15,16],[17,18,1]],[[11,12,13],[11,1,13],[11,12,13]]]
     list3 = [1,2,3,[4,5,6]]
     list4 = [[[1,2,3],[4,5,6],[7,8,9]],[1,2,3],[1,2,3],[11,12,13,[14,15,16]]]

     # [1,2]を含むかどうか調べる
     query = [1,2]

     # [1,2]のどちらか一方でも入っているか調べる例
     print(multidimension_search(list1, query, contains_all=False))  # [0, 1]
     print(multidimension_search(list2, query, contains_all=False))  # [[1, 2], [1]]
     print(multidimension_search(list3, query, contains_all=False))  # エラーメッセージ + None
     print(multidimension_search(list4, query, contains_all=False))  # エラーメッセージ + None

     # [1,2]の全てが入っているか調べる例
     print(multidimension_search(list1, query, contains_all=True))  # [0]
     print(multidimension_search(list2, query, contains_all=True))  # [[], []]
     print(multidimension_search(list3, query, contains_all=True))  # エラーメッセージ + None
     print(multidimension_search(list4, query, contains_all=True))  # エラーメッセージ + None


     # 文字列の検索テスト
     string_list1 = [["aaa","bbb","ccc"],["aaa","bbb","ccc"],["aaa","bbb","ccc"]]
     string_list2 = [["aaa","aaa","aaa"],["bbb","bbb","bbb"],["ccc","ccc","ccc"]]
     string_list3 = [[["aaaa","aaaa","aaaa"],["bbbb","bbbb","bbbb"]],[["bbb","bbb"],["cccc","cccc"]]]
     string_list4 = [[["abc","xyz"],["aaa","bbb","ccc"]],[["aaa","xyz"],["abc","abc","abc"]]]

     # "aaa","bbb","ccc"について、含まれているインデックスを検索
     string_query = ["aaa","bbb","ccc"]

     # "aaa","bbb","ccc"のどちらか一方でも入っているか調べる例
     print(multidimension_search(string_list1, string_query, contains_all=False))  # [0, 1, 2]
     print(multidimension_search(string_list2, string_query, contains_all=False))  # [0, 1, 2]
     print(multidimension_search(string_list3, string_query, contains_all=False))  # [[], [0]]
     print(multidimension_search(string_list4, string_query, contains_all=False))  # [[1], [0]]

     # "aaa","bbb","ccc"の全てが入っているか調べる例
     print(multidimension_search(string_list1, string_query, contains_all=True))  # [0, 1, 2]
     print(multidimension_search(string_list2, string_query, contains_all=True))  # []
     print(multidimension_search(string_list3, string_query, contains_all=True))  # [[], []]
     print(multidimension_search(string_list4, string_query, contains_all=True))  # [[1], []]


if __name__=="__main__":
     main()