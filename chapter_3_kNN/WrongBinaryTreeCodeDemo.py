# -*- coding: utf-8 -*-
################################### PART0 DESCRIPTION #################################
# Filename: WrongBinaryTreeCodeDemo.py
# Description: 虽然是错误的二叉树实现方法，但仍然值得参考。
#

# E-mail: ysh329@sina.com
# Create: 2016-12-03 21:46:34
# Last:
__author__ = 'yuens'


################################### PART1 IMPORT ######################################


################################### PART2 CLASS && FUNCTION ###########################

class Node(object):
    '''
    构造结点并生成二叉树。
    '''
    def __init__(self, xList):
        '''
        基于列表数据 xList 构造二叉树，
        :param xList: 一维的特征实例集
        '''
        if len(xList)==0:
            return None
        self.value = median(xList)
        # 注意左子树接受的还有等于的情况
        self.left = None if len(xList)<=1 else Node(xList=filter(lambda v:\
                                                                 v <= self.value,\
                                                                 xList)\
                                                   )
        self.right = None if len(xList)<=1 else Node(xList=filter(lambda v:\
                                                                  v > self.value,\
                                                                  xList)\
                                                    )

    def findNearest(self, root, x):
        '''
        传入根结点，找到与 x 最近的实例并返回。
        :param root: 传入的根结点
        :param x: 传入需要计算与之最近的实例点
        :return:
        '''
        # 跳过非叶子结点
        if root.value == x and root.left == root.right == None:
            return x

        # 注意左子树接受的还有等于的情况
        if x <= root.value and root.left != None:
            root = root.left
            return self.findNearest(root, x)
        # 注意左子树接受的还有等于的情况
        elif x <= root.value and root.left == None:
            return root.value
        elif root.value < x and root.right != None:
            root = root.right
            return self.findNearest(root, x)
        elif root.value < x and root.right == None:
            return root.value
        else:
            print("Error")
            return -1

    def midTravel(self, root):
        '''
        中序遍历。
        :param root:
        :return:
        '''
        if root.left != None:
            self.midTravel(root.left)

        # 跳过非叶子结点
        if root.left == root.right == None:
            print("root.value:{0}".format(root.value))

        if root.right != None:
            self.midTravel(root.right)

    def headTravel(self, root):
        '''
        前序遍历。
        :param root:
        :return:
        '''
        # 跳过非叶子结点
        if root.left == root.right == None:
            print("root.value:{0}".format(root.value))

        if root.left != None:
            self.headTravel(root.left)

        if root.right != None:
            self.headTravel(root.right)

    def tailTravel(self, root):
        '''
        后序遍历。
        :param root:
        :return:
        '''
        if root.left != None:
            self.tailTravel(root.left)

        if root.right != None:
            self.tailTravel(root.right)

        # 跳过非叶子结点
        if root.left == root.right == None:
            print("root.value:{0}".format(root.value))

def median(xList):
    '''
    计算列表 xList 的中位数并返回。若列表中元素个数为偶数，则中位数为中间两个数的均值，
    如果列表中元素个数为奇数，则中位数为列表中间的元素。
    :param xList: 输入列表 xList
    :return: 返回列表 xList 的中位数
    '''
    if not isinstance(xList, list):
        print("input variable is not list variable.")
        return -1
    xList.sort()
    tmpMidIdx = (len(xList) - 1) / 2
    if len(xList) % 2 == 0:
        midLeftIdx = len(xList) / 2
        midRightIdx = tmpMidIdx
        medianNum = (xList[midLeftIdx] + xList[midRightIdx])/2.0
        return medianNum
    else:
        medianNum = xList[tmpMidIdx]
        return medianNum

################################### PART3 TEST ########################################
# 例子
if __name__ == "__main__":
    # 参数初始化
    xList = [1, 2, 3, 4, 5, 6]

    # 实例
    root = Node(xList=xList)
    print("root.findNearest(root, 3):{0}".format(root.findNearest(root, 3)))

    # 三种序列遍历
    # 因为全部只打印叶子结点所以结果是一样的
    # 若打印全部结点则能看出不同
    print("== midTravel ==")
    root.midTravel(root)

    print("== headTravel ==")
    root.headTravel(root)

    print("== tailTravel ==")
    root.tailTravel(root)