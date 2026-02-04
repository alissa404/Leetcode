class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
        先轉十進位做相加 再轉回二進位
        int(a, 2)：將二進位字串轉成十進位整數。
        bin(...)：將相加後的整數轉回二進位字串（開頭會帶有 0b，所以要用 [2:] 去掉）。
        '''
        print(bin(int(a, 2) + int(b, 2)))
        return bin(int(a, 2) + int(b, 2))[2:]

a ="11"
b="1"

print(Solution().addBinary(a, b))