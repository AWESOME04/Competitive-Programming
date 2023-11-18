def is_beautiful(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if math.gcd(arr[i], arr[j]) > (j - i + 1):
                return False
    return True

def main():
    t = int(input())  # Number of test cases

    for _ in range(t):
        n = int(input())  # Length of array
        arr = list(map(int, input().split()))  # Elements of array

        # Check if the array is beautiful
        if is_beautiful(arr):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    import math

    main()
