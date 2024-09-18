def new_test(dir,filename,message):
  f = open(filename,"x")
  f = open(filename,"a")
  f.write(message)

new_test(.,newtest,"this is a new test") 


