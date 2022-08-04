import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr1 = set(map(int, input().split()))
arr2 = set(map(int, input().split()))

arr3 = arr1 - arr2
arr4 = arr2 - arr1

arr5 = arr3 | arr4

print(len(arr5))

