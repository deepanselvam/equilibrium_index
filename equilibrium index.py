class IndexArray:
    @staticmethod
    def equilibriumIndex(arr):
        n = len(arr)
        p = [0] * n
        p[0] = arr[0]
        for i in range(1, n):
            p[i] = p[i-1] + arr[i]
        count = 0
        min_val = float('inf')
        for i in range(1, n):
            if p[i-1] == p[n-1] - p[i]:
                count += 1
                if min_val > i:
                    min_val = i
        if count == 0:
            return -1
        return min_val

    @staticmethod
    def main():
        n = int(input())
        arr = list(map(int, input().split()))
        count = IndexArray.equilibriumIndex(arr)
        print(count)

IndexArray.main()
