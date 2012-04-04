from django.db import models
import sqlite3

# Create your models here.
class Page(models.Model):
	name= models.CharField('name', max_length=200, primary_key=True)
	content = models.TextField('Desc',max_length=500, blank=True)

class CifsShareModel(models.Model):
	ABOUT_CHOICES=(
		(u'DE',u'Department'),
		(u'GP',u'Group'),
		)
	ExportName= models.CharField('name',max_length=100)
	about= models.CharField(max_length=100,choices=ABOUT_CHOICES)



connection=sqlite3.connect('/Users/kylemartens/Desktop/FIHelpSite2/FIHelpSite/CifsShare.db')
cursor=connection.cursor()
cursor.execute('''CREATE TABLE CifsShare 
	( ExportName TEXT, GroupOrDepartment TEXT, Address TEXT)''')
cursor.execute("""insert into CifsShare
	values('FI EVAL Team', 'GP', '\\data.fi.ncsu.edu\fievalteam')""")
cursor.execute("""insert into CifsShare
	values('FI STEM Group', 'GP','\\data.fi.ncsu.edu\fistemgroup')""")
cursor.execute("""insert into CifsShare
	values('GEES', 'GP','\\data.fi.ncsu.edu\gees')""")
cursor.execute("""insert into CifsShare
	values('GISMO', 'GP','\\data.fi.ncsu.edu\gismo')""")
cursor.execute("""insert into CifsShare
	values('LEONARDO', 'GP','\\data.fi.ncsu.edu\leonardo')""")
cursor.execute("""insert into CifsShare
	values('LTBI', 'GP','\\data.fi.ncsu.edu\ltbi')""")
cursor.execute("""insert into CifsShare
	values('MINDSET', 'GP','\\data.fi.ncsu.edu\mindset')""")
cursor.execute("""insert into CifsShare
	values('MISO', 'GP','\\data.fi.ncsu.edu\miso')""")
cursor.execute("""insert into CifsShare
	values('New Learning Ecologies', 'GP','\\data.fi.ncsu.edu\newlearningecologies')""")
cursor.execute("""insert into CifsShare
	values('PTMT', 'GP','\\data.fi.ncsu.edu\ptmt')""")
cursor.execute("""insert into CifsShare
	values('VCLSU', 'GP','\\data.fi.ncsu.edu\vclsu')""")

connection.commit()
cursor.close()
