from prettytable import PrettyTable
x=PrettyTable()
import getdata as gd
stand=gd.getData(3)
x.field_names = ["Team", "Wins", "Losses", "Division","Conference"]
x.add_row([stand[0]['team'][0],stand[0]['wins'],stand[0]['losses'],stand[0]['Division'][0],stand[0]['Conference'][0]])
print(x)
class pfs(object) :
	def _str_(self) :
		return f"{self.team}