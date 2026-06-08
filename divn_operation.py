
from BaseOperation import BaseOperation

class div(BaseOperation):
 def calc(self,x,y):
  if y == 0 :
   return  "Error division by zero" 

  return x/y 