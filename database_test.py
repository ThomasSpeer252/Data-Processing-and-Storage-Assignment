from keyValueDatabase import Database

database = Database() #initialize database object


database.get('A') #returns null

database.put('A', 5) #returns null

database.begin_transaction() #start a transaction

database.put('A', 5) #add A,5 to database but it is not commited yet

database.get('A') #not found because it is not commited

database.put('A', 6)# update A in the temp database to have a new value

database.commit()#commit changes to final database

database.get('A')#print value of A

database.commit()#throws an error because no open transaction

database.rollback()#throws an error because no open transaction

database.get('B')#returns null because it is not in the final database

database.begin_transaction()#start new transaction

database.put('B', 10)#put B,10 in the temp database

database.rollback()#roll back changes

database.get('B')#Error not found because changes were rolled back
