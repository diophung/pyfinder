# pyfinder
Design POC for Python + Flask + uwsgi + nginx for scalable production 

## requirements
- conda or virtualenv
- pip
- python 3.x

## how to start
Assume you're at the root directory of this repository. Open terminal and run this:

```
chmod +x ./startserver.sh
./startserver.sh
```

Expect to see these
```
./startserver.sh
[uWSGI] getting INI configuration from uwsgi.ini
*** Starting uWSGI 2.0.18 (64bit) on [Sun Nov 15 03:53:32 2020] ***
compiled with version: 4.8.5 20150623 (Red Hat 4.8.5-39) on 15 November 2020 07:37:51
os: Linux-3.10.0-1127.18.2.el7.x86_64 #1 SMP Sun Jul 26 15:27:06 UTC 2020
nodename: vm-ce7-kde
machine: x86_64
clock source: unix
detected number of CPU cores: 8
current working directory: /home/dio/works/pyfinder
detected binary path: /home/dio/.conda/envs/pyfinder/bin/uwsgi
!!! no internal routing support, rebuild with pcre support !!!
your processes number limit is 4096
your memory page size is 4096 bytes
detected max file descriptor number: 1024
lock engine: pthread robust mutexes
thunder lock: disabled (you can enable it with --thunder-lock)
uWSGI http bound on :9090 fd 3
uwsgi socket 0 bound to UNIX address /tmp/uwsgi.sock fd 6
Python version: 3.7.9 (default, Aug 31 2020, 12:42:55)  [GCC 7.3.0]
Python main interpreter initialized at 0x1e49e10
python threads support enabled
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 416720 bytes (406 KB) for 8 cores
*** Operational MODE: preforking+threaded ***
WSGI app 0 (mountpoint='') ready in 1 seconds on interpreter 0x1e49e10 pid: 7958 (default app)
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI master process (pid: 7958)
spawned uWSGI worker 1 (pid: 7959, cores: 2)
spawned uWSGI worker 2 (pid: 7960, cores: 2)
spawned uWSGI worker 3 (pid: 7961, cores: 2)
spawned uWSGI worker 4 (pid: 7963, cores: 2)
*** Stats server enabled on :9191 fd: 21 ***
spawned uWSGI http 1 (pid: 7966)
[pid: 7961|app: 0|req: 1/1] 192.168.241.1 () {38 vars in 717 bytes} [Sun Nov 15 03:53:33 2020] GET / => generated 69 bytes in 1 msecs (HTTP/1.1 200) 2 headers in 79 bytes (2 switches on core 0)
[pid: 7961|app: 0|req: 2/2] 192.168.241.1 () {38 vars in 717 bytes} [Sun Nov 15 03:53:33 2020] GET / => generated 69 bytes in 0 msecs (HTTP/1.1 200) 2 headers in 79 bytes (1 switches on core 1)
[pid: 7961|app: 0|req: 3/3] 192.168.241.1 () {38 vars in 717 bytes} [Sun Nov 15 03:53:33 2020] GET / => generated 69 bytes in 0 msecs (HTTP/1.1 200) 2 headers in 79 bytes (1 switches on core 0)
[pid: 7961|app: 0|req: 4/4] 192.168.241.1 () {38 vars in 717 bytes} [Sun Nov 15 03:53:33 2020] GET / => generated 69 bytes in 0 msecs (HTTP/1.1 200) 2 headers in 79 bytes (1 switches on core 1)
```

## how to change uwsgi setting?
You can change the uwsgi settings by modifying its config file `uwsgi.ini`. Currently it has bare minimum configurations to run uwsgi server:
```
[uwsgi]
module = wsgi:app  # wsgi is required, app is the name of Flask callable

master = true  # true for production - a master process will spawn other and do process management
processes = 4  # number of processes that uwsgi spawn
threads = 2 # number of threads for each processes

socket=/tmp/%n.sock
chmod-socket = 660
vacuum = true

die-on-term = true
http = :9090  # port to listen
stats = :9191  # stats port (JSON stats)
```

## references
- (uWSGI latest documentation)[https://uwsgi-docs.readthedocs.io/en/latest/]
- (uWSGI Github source code)[https://github.com/unbit/uwsgi]
