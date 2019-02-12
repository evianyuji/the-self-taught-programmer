# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""
#statistics --- 数理統計関数 — Python 3.7.1rc1 ドキュメント
import statistics

#mean
nums = [1, 5, 33, 12, 46, 33, 2, 10]
print(statistics.mean(nums))

#median
print(statistics.median(nums))

#mode
print(statistics.mode(nums))

print(statistics.median_high(nums))

print(statistics.median_low(nums))

#調和平均
print(statistics.harmonic_mean(nums))

#母分散
print(statistics.pvariance(nums))

#母分散の標準偏差
print(statistics.pstdev(nums))
