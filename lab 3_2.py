# Определить иерархию и/или композицию классов/объектов
# (в соответствии с вариантом). Реализовать классы.
# Написать демонстрационную программу, в которой создаются объекты различных
# классов. Определение классов, их реализацию.
# Каждый класс должен иметь отражающее смысл название и информативный состав.
# Наследование должно применяться только тогда, когда это имеет смысл.

# Классы - Квитанция, Накладная, Документ, Чек, Дата.

class Date:
    def __init__(self, data):
        self.data=data

class Document(Date):
    def __init__ (self, Num, executor, recipient,date):
        Date.__init__(self,date)
        self.number=Num
        self.executor =executor
        self.recipient = recipient
class receipt (Document):
    def __init__ (self, sum, num, executor, recipient, date ):
        Document.__init__(self, num, executor, recipient,date)
        self.Sum=sum

class check (Document) :
    def __init__ (self, goods,num, executor, recipient, date):
        Document.__init__(self, num, executor, recipient, date)
        self.goods=goods

class invoice(Document) :
    def __init__(self,num, executor, recipient, date, Qty,cost):
        Document.__init__(self, num, executor, recipient, date)
        self.Qty = Qty
        self.cost =cost

        print (self.cost * self.Qty)

a= invoice (3,4,2,3,5,6)



