#import graphs as g
import melodicViolin as mv
import shutdown as s
import threading

### THREADING APPROACH
#t1 = threading.Thread(target=mv.main,args=(375,))
#t1.start()
#t2 = threading.Thread(target=s.violin)
#t2.start()

### NO-THREADING APPROACH
mv.main2()