#import graphs as g
import melodicPiano as mp
import shutdown as s
import threading

### THREADING APPROACH
#t1 = threading.Thread(target=mp.main,args=(375,))
#t1.start()
#t2 = threading.Thread(target=s.piano)
#t2.start()

### NO-THREADING APPROACH      
mp.main2()
