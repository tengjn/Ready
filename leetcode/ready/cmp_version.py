# def compare_versions(version1, version2):
#     v1 = list(map(int, version1.split('.')))
#     v2 = list(map(int, version2.split('.')))

#     for i in range(max(len(v1), len(v2))):
#         num1 = v1[i] if i < len(v1) else 0
#         num2 = v2[i] if i < len(v2) else 0

#         if num1 < num2:
#             return version2
#         elif num1 > num2:
#             return version1
#         else:
#             continue

#     return version1  # If the versions are equal

# def find_max_version(versions):
#     max_version = versions[0]
#     for version in versions:
#         max_version = compare_versions(max_version, version)
#     return max_version




class Solution:
    def cmp_version(self, version1, version2):
        version1 = version1.split('.')
        version2 = version2.split('.')
        version1 = [int(ver) for ver in version1]
        version2 = [int(ver) for ver in version2]
        for num1, num2 in zip(version1, version2):
            if num1 > num2:
                return True
            elif num1 < num2:
                return False
            else:
                pass
        return True
    def find_max_version(self, versions):
        max_version = versions[0]
        for version in versions[1:]:
            if self.cmp_version(version, max_version):
                max_version = version
        return max_version

a = Solution()
input_versions = ["1.2.3", "0.5.6", "1.10.1", "1.9.1", "2.0.0"]
max_version = a.find_max_version(input_versions)
print("最大的版本号是:", max_version)
