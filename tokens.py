class token(object):
    tag = ""
    value = ""
    row = 0
    column = 0
    def __init__(self, tag, value, row, column):
        self.tag = tag
        self.value = value
        self.row = row
        self.column = column
        
    def getTag(self):
        return self.tag
    def setTag(self, tag):
        self.tag = tag
    
    def getValue(self):
        return self.value
    def setValue(self, value):
        self.value = value
    
    def getRow(self):
        return self.row
    def setRow(self, row):
        self.row = row
    
    def getColumn(self):
        return self.column
    def setColumn(self, column):
        self.column = column

    def __str__(self):
        return "<"+str(self.tag)+", \""+str(self.value)+"\">\tRow: "+str(self.row)+"\tColumn:"+str(self.column)