def MD(): #Manhattan Distance
    import numpy as np
    p1=np.array([1,2,1])
    p2=np.array([0,2,2])

    d = np.linalg.norm(p2-p1,ord=1)
    print(d)

def ED(): #Euclidean Distance
    import numpy as np
    p1 = np.array([1, 3])
    p2 = np.array([4, 2])
    d = np.linalg.norm(p2-p1)
    print(round(d, 4))