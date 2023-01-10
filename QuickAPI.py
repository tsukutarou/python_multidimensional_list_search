import numpy as np

from typing import Union


"""
不規則次元を含まない2次元配列にのみ使える, helper関数への依存がないクイックAPI.
2次元のリストから任意の要素について検索してインデックスを調べることが可能.
返った結果について, item_exist_checker()で存在確認可能.

(注意!)
1次元配列や不規則次元を含む配列を入れるとエラーになります.
3次元以上の配列を入れると正しい結果が返りません.
あくまでも「2次元配列」専用のAPIです.
3次元以上の配列から検索したい場合はmultidimension_search()を使ってください.
"""

"""
入力引数:
     input_list: 要素が存在しているか調べたいリスト(またはタプル, ndarray)
     query: 調べたい要素 (リストやタプルの形で複数渡すことも可能)
     contains_all: queryの全ての要素をもつ要素のインデックスが欲しい場合はTrue.
                   デフォルトではFalse (query内のどれか一つでも該当するものを検索)

返り値: 該当する要素番号を持った1次元リスト.
"""
def two_dim_search(
                     input_list:Union[tuple,list,np.ndarray],
                     query:Union[tuple,list,np.ndarray],
                     contains_all=False
                  ):

     if contains_all:
         return [i for i,l in enumerate(input_list) if all(map(lambda x:x in l, query))]
     else:
         return [i for i,l in enumerate(input_list) if any(map(lambda x:x in l, query))]


# 動作確認用 (codes.ipynbと同じ)
def main():
     
     # 不規則次元を含まない2次元配列のみ入力可能
     list1 = [[1,2,3],[2,3,4],[3,4,5]]
     string_list1 = [["aaa","bbb","ccc"],["aaa","bbb","ccc"],["aaa","bbb","ccc"]]

     # 1,2および"aaa","bbb","ccc"を含むかどうか調べる
     query = [1,2]
     string_query = ["aaa","bbb","ccc"]

     # [1,2]のどちらか一方でも入っているか調べる例
     print(two_dim_search(list1, query, contains_all=False))  # [0, 1]

     # [1,2]の全てが入っているか調べる例
     print(two_dim_search(list1, query, contains_all=True))  # [0]

     # "aaa","bbb","ccc"のいずれか一つでも入っているか調べる例
     print(two_dim_search(string_list1, string_query, contains_all=False))  # [0, 1, 2]

     # "aaa","bbb","ccc"の全てが入っているか調べる例
     print(two_dim_search(string_list1, string_query, contains_all=True))  # [0, 1, 2]


if __name__=="__main__":
     main()