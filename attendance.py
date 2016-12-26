#FOR CURRENT from_day BOTH FROM AND TO DAY WILL BE SAME, WEEKENDS NOT ADDED YET
#PLEASE BREAK YOUR DATES RANGE WHEN A WEEKEND COMES
#INSTALL CHROME (ONE TIME PROCESS)
#USE THIS SCRIPT TO RUN CHROME (PROVIDED IN THE REPO)
# ./chromedriver 

import time
from selenium import webdriver
USER_NAME = '20003'
PASSWORD = '20003'
from_day = 20
from_month = 12
from_year = 2016
to_day = 20
to_month= 12
to_year=2016
driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://hrms.faasos.io:5005/');
time.sleep(2) # Let the user actually see something!
username = driver.find_element_by_id('username')
username.send_keys(USER_NAME)
password = driver.find_element_by_id('password')
password.send_keys(PASSWORD)
click = driver.find_element_by_id('form0')
click.submit()
time.sleep(5)
driver.find_element_by_class_name('metro-purple').click()
time.sleep(5) # Let the user actually see something!
#purpose = driver.find_element_by_id('ddlaction').click()
#time.sleep(2)
x = True
thirtyone_month = [1,3,5,7,8,10,12]
while (x):
	if ((from_month-1) == 0):
		from_month = 12
		from_year=from_year-1
	if (from_day == 0):
		if (from_month in thirtyone_month):
			from_day = 31
			from_month=from_month-1
		else:
			if ((from_month-1) == 2):
				from_day=28
				from_month=from_month-1
			else:
				from_day = 30
				from_month=from_month-1
	a = "var date='"+str(from_day)+"/"+str(from_month)+"/"+str(from_year)+"';$('#dtRegularizeDate').val(date);$('#TxtReason').val('others');$('#dtOutDate').val(date);$('#dtNewTimeOut').val('08:00 PM');$('#dtNewTimeIn').val('10:00 AM');$('#btnSaveAndClose').click()"
	login_form = driver.find_element_by_css_selector("select#ddlaction  > option[value='/Attendance/AttendanceApplication']").click()
	date = driver.find_element_by_id('dtRegularizeDate')
	driver.execute_script(a);
	time.sleep(5)
	find_element_by_id('btnAdd').click()
	time.sleep(5)
	from_day=from_day-1;
	if (from_day < to_day):
		x=False
time.sleep(5)
driver.quit()