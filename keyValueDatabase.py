class Database:

    def __init__(self):
        self.database = []#main database and temp database for uncommitted changes and committed changes
        self.temp = []
        
        self.transaction_in_progess = False
        self.key = ''
        self.value = 0
        
    def begin_transaction(self):
        if self.transaction_in_progess == False:
            self.transaction_in_progess = True
            print('Transaction Started\n')

        elif self.transaction_in_progess == True:
            print('Error. Transaction already started;\n')
                  
    def put(self, key, value):
        if self.transaction_in_progess == True:
            #if the key is in the temp database, update its value
            found = False
            for i in range(0, len(self.temp)):
                if key == self.temp[i][0]:
                    self.temp[i][1] = value
                    print(f'Entry updated. Key:{self.temp[i][0]} Value:{self.temp[i][1]}\n')
                    found = True
            
            if found == False: #if not, simply add it to the temp database
                self.temp.append([key,value])
                print(f'Key:{key} Value:{value} added to database\n')

            
                
        elif self.transaction_in_progess == False:
            print('Error. transaction not in progress\n')
            return None
        
    def get(self, key):
        
        found = False
        for i in range(0, len(self.database)):#find the key in the database and return the value
            if key == self.database[i][0]:
                print(f'Found! Key:{self.database[i][0]} Value:{self.database[i][1]}\n')
                found = True

        if found == False: #error if not found
            print('Error. Not found\n')
            return None
        
            
        

    def commit(self):
        if self.transaction_in_progess == True:
            for i in range(0, len(self.temp)):# commit all temp changes to final database
                self.database.append(self.temp[i])
                i += 1
            self.transaction_in_progess = False
            self.temp == []
        else:
            print('Error. transaction not in progress\n')
            return None
        
    def rollback(self):
        if self.transaction_in_progess == True:# rollback all changes in the temp database
            print('Canceling transaction and rolling back changes...\n')
            self.temp == []
            self.transaction_in_progess = False
        else:
            print('Error. transaction not in progress\n')
            return None
        
