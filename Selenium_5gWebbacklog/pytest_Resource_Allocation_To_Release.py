#-*-coding=utf-8

#coding=utf-8
#2017/7/18
#author:Sunxia
#task:Release Milestones & Resource Allocation To Release

import pytest
from Selenium_Resource_Allocation_To_Release import Selenium_Resource_Allocation_To_Release

class TestResource_Allocation_To_Release:

    def setup_class(self):
        self.test = Selenium_Resource_Allocation_To_Release()

    def teardown_class(self):
        self.test.driver.quit()

    # 验证3个head标签是否正常显示
    def test_Find_title_Resource_Allocation_To_Release(self):
        assert ("Resource Allocation To Release", "Pipeline Info","Pipeline Charts") == self.test.Find_title_Resource_Allocation_To_Release()

    # 验证Release mgmt和Release Milestonss等文字是否正常显示
    def test_Find_link_Test(self):
        assert "Release mgmt.", "Release Milestones" == self.test.Find_link_Test()

    # 点击Home文字链接
    def test_Click_Home(self):
        str = self.test.Click_Home()
        assert "Success" == str

    # 点击问号按钮并关闭
    def test_Click_question_Button(self):
        str = self.test.Click_question_Button()
        assert "Success" == str

    # 测试第一个图形按钮
    def test_Click_First_Button(self):
        str = self.test.Click_First_Button()
        assert "Success" == str
        self.test.driver.refresh()

    # 测试第二个图形按钮
    def test_Click_Second_Button(self):
        str = self.test.Click_Second_Button()
        assert "Success" == str
        self.test.driver.refresh()

    # 测试第三个图形按钮
    def test_Click_Third_Button(self):
        str = self.test.Click_Third_Button()
        assert "Success" == str
        self.test.driver.refresh()

    # 测试第四个图形按钮
    def test_Click_Fourth_Button(self):
        str = self.test.Click_Fourth_Button()
        assert "Success" == str
        self.test.driver.refresh()

    # 验证搜索功能
    def test_Search_Send_Keys(self):
        str = self.test.Search_Send_Keys()
        assert "Success" == str

    # 选择显示多少条信息
    def test_Select_Show_Num(self):
        str = self.test.Select_Show_Num()
        assert "Success" == str

    # Pipeline Info时间选择测试
    def test_Date_Select(self):
        str = self.test.Date_Select()
        assert "Success" == str

    # 检查表格完整性
    def test_Verify_Table_Integrity(self):
        self.test.driver.refresh()
        table = self.test.Verify_Table_Integrity()
        for row in table:
            for column in row:
                assert column != ""

    # 判断图表是否加载
    def test_Canvas_is_Showed(self):
        str = self.test.Canvas_is_Showed()
        assert "Success" == str

    # 图下方文字点击
    def test_Under_Canvas_Click(self):
        str = self.test.Under_Canvas_Click()
        assert "Success" == str
        self.test.driver.refresh()

    # 表格页面切换
    def test_Table_Page_Change(self):
        str = self.test.Table_Page_Change()
        assert "Success" == str

if __name__ == '__main__':
    pytest.main("-q test_baidu.py")

