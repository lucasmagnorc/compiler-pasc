class ErrorMessage(object):
    tag = ""
    message = ""
    row = 0
    column = 0
    def __init__(self, tag, message, row, column):
        self.tag = tag
        self.message = message
        self.row = row
        self.column = column
        
    def getTag(self):
        return str(self.tag)
    def setTag(self, tag):
        self.tag = tag
    
    def getMessage(self):
        return self.message
    def setMessage(self, message):
        self.message = message
    
    def getRow(self):
        return self.row
    def setRow(self, row):
        self.row = row
    
    def getColumn(self):
        return self.column
    def setColumn(self, column):
        self.column = column

    def __str__(self):
        return ".::"+str(self.tag)+" \""+str(self.message)+"\"::.\tRow: "+str(self.row)+"\tColumn:"+str(self.column)