#coding=utf-8
#2017/7/18
#author:Sunxia
#task:Release Milestones & Resource Allocation To Release

from selenium import webdriver
import time

class Selenium_Release_Milestones:

    #构造函数,加载Webbacklog页面,并跳转到Release Milestones页面
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url="http://127.0.0.1:8000/webbacklog/"
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(1)
        self.driver.find_element_by_link_text("Release mgmt.").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Release Milestones").click()
        time.sleep(1)

    #返回页面title
    def Find_title_Release_Milestones(self):
        return self.driver.find_element_by_tag_name("h1").text , self.driver.find_element_by_tag_name("h3").text

    #点击Home文字链接
    def Click_Home(self):
        string = ""
        try:
            self.driver.find_element_by_link_text("Home").click();
            time.sleep(1)
            self.driver.back()
            string = "Success"
        except:
            string = "Error :Element in method 'Click_Home' Not Founded"
        return string

     # 验证Release mgmt和Release Milestonss文字是否显示
    def Find_link_Test(self):
        text1 = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/section[1]/ol/li[2]").text
        text2 = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/section[1]/ol/li[3]").text
        return text1,text2

    #点击问号按钮并关闭
    def Click_question_Button(self):
        string = ""
        try:
            self.driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[1]/div[1]/div/div[1]/i").click();
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='milestoneModal']/div/div/div/div/div[1]/button").click()
            string = "Success"
        except:
            string = "Error :Element in method 'Click_question_Button' Not Founded"
        return string

    #验证搜索功能
    def Search_Send_Keys(self):
        string = ""
        try:
            self.driver.find_element_by_xpath("//*[@id='milestoneTable_filter']/label/input").send_keys("nokia")
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='milestoneTable_filter']/label/input").clear()
            self.driver.find_element_by_xpath("//*[@id='milestoneTable_filter']/label/input").send_keys("s")
            string = "Success"
        except:
            string = "Error :Element in method 'Search_Send_Keys' Not Founded"
        return string

    #点击每个表头
    def Click_table_title(self):
        string = ""
        try:
            self.driver.find_element_by_xpath("//*[@id='milestoneTable']/thead/tr/th[1]").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='milestoneTable']/thead/tr/th[1]").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='milestoneTable']/thead/tr/th[2]").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='milestoneTable']/thead/tr/th[2]").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='milestoneTable']/thead/tr/th[3]").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='milestoneTable']/thead/tr/th[3]").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='milestoneTable']/thead/tr/th[4]").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='milestoneTable']/thead/tr/th[4]").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='milestoneTable']/thead/tr/th[5]").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='milestoneTable']/thead/tr/th[5]").click()
            string = "Success"
        except:
            string = "Error :Element in method 'Click_table_title' Not Founded"
        return string

    #验证edit功能，并在空白处添加日期后删除
    def Click_Edit(self):
        string = ""
        try:
            self.driver.find_element_by_xpath("//*[@id='milestoneTable']/tbody/tr[1]/td[6]/buttn[1]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='milestoneTable']/tbody/tr[1]/td[2]/div/input").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[2]/td[3]").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='milestoneTable']/tbody/tr[1]/td[2]/div/input").clear()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='milestoneTable']/tbody/tr[1]/td[6]/buttn[2]").click()
            string = "Success"
        except:
            string = "Error :Element in method 'Click_Edit' Not Founded"
        return string

    #选择显示多少条信息
    def Select_Show_Num(self):
        string = ""
        try:
            self.driver.find_element_by_xpath("//*[@id='milestoneTable_length']/label/select").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='milestoneTable_length']/label/select/option[2]").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='milestoneTable_length']/label/select/option[3]").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='milestoneTable_length']/label/select/option[4]").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='milestoneTable_length']/label/select").click()
            string = "Success"
        except:
            string = "Error :Element in method 'Select_Show_Num' Not Founded"
        return string

    #点击Nokia文字链接
    def Click_Nokia(self):
        string = ""
        try:
            self.driver.find_element_by_link_text("Nokia").click();
            time.sleep(1)
            self.driver.back()
            string = "Success"
        except:
            string = "Error :Element in method 'Click_Nokia' Not Founded"
        return string


    #验证表格中数据是否正确
    def Verify_Table_Data(self):
        return self.driver.find_element_by_xpath("//*[@id='milestoneTable']/tbody/tr[1]/td[1]/span").text

    # 检查表格完整性
    def Verify_Table_Integrity(self):
        table = []
        time.sleep(3)
        table_loc = self.driver.find_element_by_xpath("//*[@id='milestoneTable']/tbody")
        rows = len(table_loc.find_elements_by_tag_name("tr"))
        columns = len(
            table_loc.find_element_by_xpath("//*[@id='milestoneTable']/tbody/tr[1]").find_elements_by_tag_name("td"))
        for row in range(1, rows + 1):
            table_row = []
            for column in range(1, columns + 1):
                xpath = "//*[@id='milestoneTable']/tbody/tr[" + str(row) + "]/td[" + str(column) + "]"
                table_row.append(self.driver.find_element_by_xpath(xpath).text)
            table.append(table_row)
        return table

    #析构函数
    def __del__(self):
        self.driver.quit()

'''
test = Selenium_Release_Milestones()
test.Load()
test.Click_to_Release_Milestones()
test.Find_link_Test()
'''






