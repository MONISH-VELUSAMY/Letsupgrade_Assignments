#original func
def div(a,b):
  print(a/b)
#decorator
def mod_div(fun):
  def inner(a,b):
     if a<b:
        a,b=b,a
     fun(a,b)
  return inner

div=mod_div(div)
div(2,4)
