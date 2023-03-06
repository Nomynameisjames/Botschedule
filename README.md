				# BotSchedule
		## BotSchedule: Automating Learning and Task Management
**"Streamlining and personalising your learning journey through self-customised scheduling and resource recommendations."




## Features

- [x] Elegant and intuitive API 
- [x] Rich preset rules
- [x] Powerful management mechanism
- [x] Detailed execution history
- [x] Thread safe
- [x] Complete documentation
- [x] ~100%+ test coverage

### Why You Should Use Schedule

| Features | Timer | DispatchSourceTimer | Schedule |
| --- | :---: | :---: | :---: |
| ⏰ Self-customised schedule | ✓ | ✓ | ✓ |
| 📆 Allows users to select a specific area of study, pick a course, set a date, and reminder | ✓ | | ✓ |
| 🌈 Provides recommendations of websites and resources to help maximise study on the topic area | | | ✓ |
| 🗣️ Plots a weekly and monthly graph to show performance based on daily task average and targets completed | | | ✓ |
| 🏷 Includes a chatbot functionality using the OpenAI API for assistance | | | ✓ |
| 📝 Allows users to enter a specific course of study, set a reminder of the most conducive day and time, and automatically breaks down the course into topics covering the subject area | | | ✓ |
| 🎡 Includes the functionalities mentioned in the self-customisable schedule function | | ✓ | ✓ |
| 🚦 Suspend, Resume, Cancel | | ✓ | ✓ |
| 🍰 Fully Schedule Automation | | | ✓ |
| 🍰 Allows users to pick a subject area or programming language (e.g. "Python") and automatically enrol in the 30-day Python programming coding challenge | | | ✓ |
| 🍰 Breaks down the course into daily topics geared towards helping the user achieve set objectives | | | ✓ |
| 🍰 Automatically sends resource recommendations when the set date and time reminder is due | | | ✓ |
| 🍰 Automatically assesses the user based on the amount of targets completed and average set | | | ✓ |
| 🍰 Includes chatbot functionalities for further assistance | | | ✓ |



## Usage

### Overview

Scheduling a task has never been so elegant and intuitive, all you have to do is:

```swift






#Requirements:

*.	set up a virtual environment which enables you install packages and modules seperate from your system-wide environment
	rirst install a venv module with the command
	''' python3 -m pip install virtualenv '''
	Create a new virtual environment
	'''  python3 -m venv myenv '''
	Activate the virtual environment
 	'''  source myenv/bin/activate '''
	

*.	setup a mysql database 
	''' pip3 install mysql-client '''
	


    This project comes with various setup scripts to support automation, especially
    during maintanence or to scale the entire project.  The following files are the
     setupfiles along with a brief explanation:
  
    * **`dev/setup.sql`:** Drops test and dev databases, and then reinitializes
     the datbase.
  
    * Usage: `$ cat dev/setup.sql | mysql -uroot -p`
  
    * **`setup_mysql_dev.sql`:** initialiezs dev database with mysql for testing
 
    * Usage: `$ cat setup_mysql_dev.sql | mysql -uroot -p`
 
    * **`setup_mysql_test.sql`:** initializes test database with mysql for testing
  
    * Usage: `$ cat setup_mysql_test.sql | mysql -uroot -p`

	connect to your mysql database using sqlalchemy module
	''' pip3 install sqlalchemy '''


*.	log on to the twilio website and create an API auth key on your terminal install the twilio package using
	''' pip3 install twilio '''
	this enables use send a reminder directly to your specified phone number using the twilio API

*.	create an OpenAI API auth key to enable you access the Chatbot feature
	install openai by running the command
	''' pip3 install openai '''

*.	install the matplotlib module to help plot graphical representation of your average over a period of time
	''' pip3 install matplotlib '''

 
