import pandas as pd
import base64

class UserAdminister():
    def __init__(self,dataAdd = './source/userRecorde/userDatabase.csv'):
        self.Add = dataAdd
        self.database = pd.read_csv(self.Add)
        print(self.database)

    def usernameRepeatJudge(self, username):
        index = self.database[self.database.userName == username].index.tolist()

        if (len(index)>0):
            return True
        else:
            return False

    def dataIn(self,username,password,question,answer):
        password = str(base64.b64encode(bytes(password, 'ascii')),encoding='utf-8')
        answer = str(base64.b64encode(bytes(answer, 'ascii')),encoding='utf-8')
        row = {'userName': username, 'password': password, 'questionOp': question, 'answer': answer}
        print(row)
        self.database = self.database.append(row, ignore_index=True)
        self.database.to_csv(self.Add, index=0)

    def logIn(self,username,password):
        print(password)
        index = self.database[self.database.userName == username].index.tolist()
        for i in index:
            print(str(base64.b64decode(self.database.iloc[i].password),encoding='utf-8'))
            if str(base64.b64decode(self.database.iloc[i].password),encoding='utf-8') == password:
                self.id = i
                return True
        return False


    def flesh(self):
        self.database = pd.read_csv(self.Add)

    def codeChange(self,newPass):
        d_index = list(self.database.columns).index('password')
        self.database.iloc[self.id, d_index] = str(base64.b64encode(bytes(newPass, 'ascii')),encoding='utf-8')
        self.database.to_csv(self.Add, index=0)

    def isExit(self,username):
        index = self.database[self.database.userName == username].index.tolist()
        if len(index) > 0:
            return True
        else:
            return False
    def findback(self,username,question,answer):
        index = self.database[self.database.userName == username].index.tolist()
        self.id = index[0]
        print(str(base64.b64decode(self.database.iloc[self.id].answer), encoding='utf-8'))
        print(self.database.iloc[self.id].questionOp)
        if str(base64.b64decode(self.database.iloc[self.id].answer), encoding='utf-8') == answer and question == self.database.iloc[self.id].questionOp:
            return True
        else:
            return False

class UserInf():
    def __init__(self, datapath='./source/userRecorde/userDatabase.csv'):
        self.datapath = datapath
        try:
            self.data = pd.read_csv(self.datapath)
        except FileNotFoundError:
            self.datapath = 'userDatabase.csv'
            self.data = pd.read_csv(self.datapath)
        self.data['password'] = self.data['password'].apply(lambda x: str(base64.b64decode(x), encoding='utf-8'))
        self.data['answer'] = self.data['answer'].apply(lambda x: str(base64.b64decode(x), encoding='utf-8'))

    def downLoadUserInf(self, filepath):
        try:
            self.data.to_csv(filepath, index=0, encoding='gbk')
            return True
        except:
            return False

    def retrievePassword(self, username):
        #retrieve Password need your username
        index = self.data[self.data.userName == username].index.tolist()
        if index != []:
            return self.data.iloc[index[0]].password
        else:
            return False

    def changePassword(self, username, newpass):
        index = self.data[self.data.userName == username].index.tolist()
        if index != []:
            for i in range(len(index)):
                self.data.loc[index[i],'password'] = newpass
            self.data['password'] = self.data['password'].apply(lambda x: str(base64.b64encode(bytes(x, 'ascii')), encoding='utf-8'))
            self.data['answer'] = self.data['answer'].apply(lambda x: str(base64.b64encode(bytes(x, 'ascii')), encoding='utf-8'))
            self.data.to_csv(self.datapath, index=0)
            self.data['password'] = self.data['password'].apply(lambda x: str(base64.b64decode(x), encoding='utf-8'))
            self.data['answer'] = self.data['answer'].apply(lambda x: str(base64.b64decode(x), encoding='utf-8'))
            return True
        else:
            return False

    def changeQuestion(self, username, newQuestion, newAnswer):
        index = self.data[self.data.userName == username].index.tolist()
        if index != []:
            for i in range(len(index)):
                self.data.loc[index[i],'questionOp'] = newQuestion
                self.data.loc[index[i],'answer'] = newAnswer
            self.data['password'] = self.data['password'].apply(lambda x: str(base64.b64encode(bytes(x, 'ascii')), encoding='utf-8'))
            self.data['answer'] = self.data['answer'].apply(lambda x: str(base64.b64encode(bytes(x, 'ascii')), encoding='utf-8'))
            self.data.to_csv(self.datapath, index=0)
            self.data['password'] = self.data['password'].apply(lambda x: str(base64.b64decode(x), encoding='utf-8'))
            self.data['answer'] = self.data['answer'].apply(lambda x: str(base64.b64decode(x), encoding='utf-8'))
            return True
        else:
            return False

if __name__ == "__main__":
    new = UserAdminister('userDatabase.csv')
    new.dataIn('liyihui5', '123456', '你的英文名', 'lekardor')

    # new.findback("liyihui1","你的英文名",'lekardor')
    # #new.logIn("lekardor","1234567")
    # new.codeChange('12345678')
    # print(new.logIn("lekardor","12345678"))
