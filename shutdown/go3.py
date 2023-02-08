#import graphs as g
import rhythm as r
import shutdown as s
import threading

### THREADING APPROACH
#t1 = threading.Thread(target=r.main,args=(375,))
#t1.start()
#t2 = threading.Thread(target=s.drums)
#t2.start()

### NO-THREADING APPROACH
r.main2()
