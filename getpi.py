# import redis
import time
# pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
# r = redis.Redis(host='localhost', port=6379, decode_responses=True)  
def pi(n):
    t=n+10
    b=10**t
    x1=b*4//5
    x2=b // -239
    s=x1+x2
    n*=2
    for i in range(3,n,2):
        x1 //= -25
        x2//= -57121
        x=(x1+x2)//i
        s+=x
        print(i)
    pai=s*4
    pai//=10**10
    # r.set('pi', pai) 
    # return pai
# print(pi(10000))

#pi(1000)
pi(10**10000000000000000000000000000000000000000000000000000000)
# k=10
# while True:
#     time.sleep(2)
#     pi(k)
#     k=k+1

# print(r.get('pi'))
