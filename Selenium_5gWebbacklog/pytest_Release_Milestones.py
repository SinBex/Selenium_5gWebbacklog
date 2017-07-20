#-*-coding=utf-8

#coding=utf-8
#2017/7/18
#author:Sunxia
#task:Release Milestones & Resource Allocation To Release

import pytest
from Selenium_Release_Milestones import Selenium_Release_Milestones

class TestRelease_Milestones:
    def setup_class(self):
        self.test = Selenium_Release_Milestones()

    # 点击Home文字链接
    def test_Click_Home(self):
         str = self.test.Click_Home()
         assert "Success" == str

    # 点击问号按钮并关闭
    def test_Click_question_Button(self):
         str = self.test.Click_question_Button()
         assert "Success" == str

    # 验证搜索功能
    def test_Search_Send_Keys(self):
         str = self.test.Search_Send_Keys()
         assert "Success" == str

    # 点击每个表头
    def test_Click_table_title(self):
        str = self.test.Click_table_title()
        assert  "Success" == str

    # 验证edit功能，并在空白处添加日期后删除
    def test_Click_Edit(self):
        str = self.test.Click_Edit()
        assert "Success" == str

    # 返回页面title
    def test_Find_title_Release_Milestones(self):
        assert "Release Milestones", "Release Milestone Table" == self.test.Click_to_Release_Milestones()

    # 验证Release mgmt和Release Milestonss等文字是否正常显示
    def test_Find_link_Test(self):
        assert "Release mgmt.", "Release Milestones" == self.test.Find_link_Test()

    # 选择显示多少条信息
    def test_Select_Show_Num(self):
        str = self.test.Select_Show_Num()
        assert "Success" == str

    # 点击Nokia文字链接
    def test_Click_Nokia(self):
        str = self.test.Click_Nokia()
        assert "Success" == str

    # 验证表格中数据是否正确
    def test_Verify_Table_Data(self):
        assert "5G16" == self.test.Verify_Table_Data()

    # 检查表格完整性
    def test_Verify_Table_Integrity(self):
        self.test.driver.refresh()
        table = self.test.Verify_Table_Integrity()
        for row in table:
            assert row[0] != ""

    def teardown_class(self):
        self.test.driver.quit()

if __name__ == '__main__':
    pytest.main("-q test_baidu.py")

