#!/usr/bin/python
# coding=utf-8

import os


# 删除path
def deleteFile(path):
    # 递归地删除目录。如果子目录成功被删除，则将会成功删除父目录，子目录没成功删除，将抛异常。
    os.removedirs(path)
    return


# 遍历文件夹
def walkFile(file):
    paths = []
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            # print(os.path.join(root, f))
            paths.append(os.path.join(root, f))

        # 遍历所有的文件夹
        # for d in dirs:
        #     print(os.path.join(root, d))
    return paths


def main():
    paths = walkFile("./")
    for f in paths:
        if f.startswith("./._"):
            # 删除文件，可使用以下两种方法。
            os.remove(f)
            print("delete file " + f)
            # os.unlink(path)


if __name__ == '__main__':
    main()
