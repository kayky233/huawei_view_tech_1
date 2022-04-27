# This is a sample Python script.
import numpy as np
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def findpeak(arr):
    # Use a breakpoint in the code line below to debug your script.
    arr_temp = arr.copy()
    peak_index_temp = []
    i =0
    k = len(arr_temp)-1
    while i < k:
            # 寻找峰的起点
            if arr_temp[i+1] > arr_temp[i]:
                # 从峰的起点的下一个点开始寻找峰，直到找到下降点
                potential_peak_index = i+1
                m = potential_peak_index
                # 开始寻找下降的点，并更新峰位信息，若有大于potential_index的点，则将峰位更新至此
                while arr_temp[m+1]>=arr_temp[m] and m < len(arr_temp):
                    # 更新m,要先更新m，否则容易漏掉峰的最后一个点
                    m+=1
                    if arr_temp[m] > arr_temp[potential_peak_index]:
                        potential_peak_index = m
                peak_index_temp.append(potential_peak_index)
                #此处m为开始下降前的前一个index,下一次查找从下降点重新开始
                i = m + 1
            else:
                i+=1
    print("done")  # Press Ctrl+F8 to toggle the breakpoint.
    return peak_index_temp




# 华为实习一轮技术面，寻找峰或高台，并返回峰所在的index 或高台所在的第一个起始点
if __name__ == '__main__':
    array = [1,1,2,2,3,3,2,2,1,3,4,5,3,1]
    peak_index = findpeak(array)
    print(peak_index)
    print("done")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
