class Baoku():
    def __init__(self,name):
        '''初始化宝库名，和一个空的宝库,宝库可能有的宝物及概率'''
        self.name = name
        self.baoku = []
        self.gai_lv_shuxing = [[50,"石头"],[25,"铜"],[15,"铁"],[7,"银"],[3,"金"]]

    def gailv_jisuan(self,gai_lv,jiazhi):
        '''输入比重，和对应的价值宝物'''
        for i in range(gai_lv):
            # gai_lv 这里代表循环次数，50就循环了50次(append了50次)
                self.baoku.append(jiazhi)

    def baoku_tianchong(self):
        """宝库填充"""
        for i in self.gai_lv_shuxing:
            self.gailv_jisuan(i[0],i[1])
        # 返回一个填充后的宝库
        return self.baoku