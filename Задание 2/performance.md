# С Redis
wrk -t12 -c400 -d30s --latency http://messenger:8000/get/get?id=15
root@33608b8afeb5:/# wrk -t12 -c400 -d30s --latency http://messenger:8000/get/get?id=15
Running 30s test @ http://messenger:8000/get/get?id=15
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   687.97ms  476.39ms   1.99s    69.58%
    Req/Sec    35.01     29.55   360.00     87.87%
  Latency Distribution
     50%  543.63ms
     75%    1.09s 
     90%    1.28s
     99%    1.90s 
  11089 requests in 30.15s, 3.62MB read
  Socket errors: connect 0, read 0, write 0, timeout 924
Requests/sec:    367.85
Transfer/sec:    122.86KB

# Без Redis
root@33608b8afeb5:/# wrk -t12 -c400 -d30s --latency http://messenger:8000/get/get?id=15
Running 30s test @ http://messenger:8000/get/get?id=15
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   659.81ms  667.93ms   2.00s    79.26%
    Req/Sec    16.95     13.16    90.00     79.16%
  Latency Distribution
     50%  196.24ms
     75%    1.14s 
     90%    1.81s
     99%    1.96s
  3676 requests in 30.10s, 1.20MB read
  Socket errors: connect 0, read 0, write 0, timeout 1757
Requests/sec:    122.13
Transfer/sec:     40.79KB