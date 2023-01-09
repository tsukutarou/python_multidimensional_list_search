from helper import nest_depth
from multidimension_search import multidimension_search


# 出力結果をboolで確認する拡張関数
"""
入力引数:
     search_result: multidimension_search()の返り値.

返り値:
     bool値. 検索した要素が存在する時はTrue, 存在していないときはFalse.
"""
def item_exist_checker(search_result):

     if nest_depth(search_result) == 0:
         if search_result == 0:
            return True
         else:
            return bool(search_result)
     else:
         return any([item_exist_checker(res) for res in search_result])


# 動作確認 (codes.ipynbと同じ)
def main():

     list1 = [[1,2,3],[2,3,4],[3,4,5]]
     list3 = [1,2,3,[4,5,6]]

     string_list1 = [["aaa","bbb","ccc"],["aaa","bbb","ccc"],["aaa","bbb","ccc"]]
     string_list3 = [[["aaaa","aaaa","aaaa"],["bbbb","bbbb","bbbb"]],[["bbb","bbb"],["cccc","cccc"]]]

     query = [1,2]
     string_query = ["aaa","bbb","ccc"]

     search_result1 = multidimension_search(list1, query, contains_all=True)
     search_result2 = multidimension_search(list3, query, contains_all=True)
     search_result3 = multidimension_search(string_list1, string_query, contains_all=True)
     search_result4 = multidimension_search(string_list3, string_query, contains_all=True)

     print(search_result1)
     print(search_result2)
     print(search_result3)
     print(search_result4)

     print(item_exist_checker(search_result1))  # [0] -> True (item exists)
     print(item_exist_checker(search_result2))  # None -> False (item doesn't exists)
     print(item_exist_checker(search_result3))  # [0, 1, 2] -> True (item exists)
     print(item_exist_checker(search_result4))  # [[], []] -> False (item doesn't exists)


if __name__=="__main__":
     main()