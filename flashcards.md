# Flashcards

Format: `- [lesson] Q: ... | A: one line | added: YYYY-MM-DD | status: new/weak/ok`
`/quiz review` drills cards marked new or weak; mark `ok` after two correct answers in a row.

- [S01] Q: Server bound to 127.0.0.1:8000 vs 0.0.0.0:8000: who can reach each? | A: 127.0.0.1 only matches packets from the same machine (loopback); 0.0.0.0 = every interface, so the LAN can reach it | added: 2026-11-02 | status: weak
- [S02] Q: RTT 200 ms, new TCP connection + one tiny request: minimum time to response? | A: ~400 ms = 1 RTT handshake (SYN, SYN-ACK; ACK rides with request) + 1 RTT request/response | added: 2026-11-02 | status: weak
- [S02] Q: Client send(2 KB); server recv(4096) once. Guaranteed all 2 KB? | A: No. recv returns whatever is in the OS buffer now; TCP keeps byte order, not send boundaries; loop until you have a full message (framing) | added: 2026-11-02 | status: new
