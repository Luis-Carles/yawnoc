#import graphs as g
import bass as b
import shutdown as s
import threading

### THREADING APPROACH
#t1 = threading.Thread(target=b.main,args=(375,))
#t1.start()
#t2 = threading.Thread(target=s.bassFS)
#t2.start()

### NO-THREADING APPROACH
b.main2()