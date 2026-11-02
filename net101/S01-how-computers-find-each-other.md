# S01 — How computers find each other (IP, ports, packets)
> ⏱ 10–15 min · Day 1 · Passive (reading + 3 commands) · Next: S02

## The one-sentence version
A backend is **a program that waits on a port for other programs to send it bytes**. This
session covers what "a port" means and how bytes get to it.

## 1. IP address = the building's street address
Every machine on a network has an **IP address**, e.g. `142.250.183.14`. Packets are delivered
to an IP the same way a letter is delivered to a street address.

Two special addresses you'll use daily:
| Address | Meaning |
|---|---|
| `127.0.0.1` (a.k.a. `localhost`) | "this same machine". Traffic never leaves your laptop. |
| `0.0.0.0` (when a server *listens*) | "accept connections on every network card I have" |

## 2. Port = the apartment number
One machine runs many programs that talk on the network: browser, Teams, Postgres. The IP gets
the packet to the **machine**; the **port** (a number 0–65535) gets it to the right **program**.

```
 142.250.183.14 : 443
 └── which machine ┘ └ which program on that machine (HTTPS server)
```
Well-known ports: 80 = HTTP, 443 = HTTPS, 5432 = Postgres, 6379 = Redis, 8000/8080 = "my dev server".
When FastAPI says `Uvicorn running on http://127.0.0.1:8000`, it means: *a program on this machine
is waiting for bytes on apartment 8000.*

## 3. Packets = the network delivers small envelopes, not whole files
The network doesn't move "a request" or "a file". It moves **packets**: chunks of roughly 1,500
bytes, each stamped with source IP:port and destination IP:port. A 3 MB PDF upload becomes about
2,000 packets. The network makes **no promises** about them:
- packets can get **lost**,
- arrive **out of order**,
- arrive **twice**.

Keep that list in mind; S02 is about the protocol (TCP) that hides all three from you.

## 4. DNS = the phone book
You type `api.openai.com`, not an IP. **DNS** turns the name into an IP before anything else
happens. (Interview trivia: "what happens when you type a URL" starts with DNS.)

## 5. The layer cake (just enough to not be scared of it)
```
 Your code (FastAPI, requests)        <- you live here
 HTTP          "GET /health"          <- text format for requests/responses   (S05)
 TCP           reliable byte stream   <- hides loss/reordering, uses ports     (S02)
 IP            packets to an address  <- best-effort delivery between machines
 Wi-Fi/Ethernet  actual signals        <- not your problem
```
Each layer only talks to the one directly below it. HTTP doesn't know packets exist; it just
writes text into TCP.

## Try it (Windows terminal, all read-only, safe on a work laptop)
```powershell
nslookup example.com                 # DNS: name -> IP
netstat -an | findstr LISTENING      # every program on your machine waiting on a port
curl.exe -v http://example.com       # watch it connect to IP:80 then speak HTTP
```
⚠ Type `curl.exe`, not `curl`: in Windows PowerShell 5.1, `curl` is an alias for
`Invoke-WebRequest`, which hides the connection details and asks a security prompt.
In the `netstat` output, find a line like `TCP 127.0.0.1:XXXXX ... LISTENING`. That's a
program on your laptop acting as a server right now.

## Check yourself (answer in chat or out loud)
1. Postgres and Redis run on the same server. How does a packet know which of the two it's for?
by the port number 
2. What's the difference between a server listening on `127.0.0.1:8000` and one listening on
   `0.0.0.0:8000`? Which one can your phone on the same Wi-Fi reach?
   i guess the second one ,since it accepts connection for every card it has
3. Name the three bad things the network can do to packets.
   losing packets, sending it twice, losing order



   PS C:\> cd C:\Users\Jeevan.Fernandes\Downloads\
PS C:\Users\Jeevan.Fernandes\Downloads> nslookup google.com
Server:  ads.novigo.com
Address:  172.16.20.15

Non-authoritative answer:
Name:    google.com
Addresses:  2404:6800:4000:1010::71
          2404:6800:4000:1010::8b
          2404:6800:4000:1010::65
          2404:6800:4000:1010::66
          142.251.106.102
          142.251.106.100
          142.251.106.101
          142.251.106.139
          142.251.106.113
          142.251.106.138

PS C:\Users\Jeevan.Fernandes\Downloads> netstat -an | findstr LISTENING
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING
  TCP    0.0.0.0:3389           0.0.0.0:0              LISTENING
  TCP    0.0.0.0:5040           0.0.0.0:0              LISTENING
  TCP    0.0.0.0:5432           0.0.0.0:0              LISTENING
  TCP    0.0.0.0:5800           0.0.0.0:0              LISTENING
  TCP    0.0.0.0:5900           0.0.0.0:0              LISTENING
  TCP    0.0.0.0:7680           0.0.0.0:0              LISTENING
  TCP    0.0.0.0:49664          0.0.0.0:0              LISTENING
  TCP    0.0.0.0:49665          0.0.0.0:0              LISTENING
  TCP    0.0.0.0:49666          0.0.0.0:0              LISTENING
  TCP    0.0.0.0:49667          0.0.0.0:0              LISTENING
  TCP    0.0.0.0:49668          0.0.0.0:0              LISTENING
  TCP    0.0.0.0:49669          0.0.0.0:0              LISTENING
  TCP    0.0.0.0:49674          0.0.0.0:0              LISTENING
  TCP    0.0.0.0:49675          0.0.0.0:0              LISTENING
  TCP    127.0.0.1:4502         0.0.0.0:0              LISTENING
  TCP    127.0.0.1:17165        0.0.0.0:0              LISTENING
  TCP    127.0.0.1:30523        0.0.0.0:0              LISTENING
  TCP    127.0.0.1:40071        0.0.0.0:0              LISTENING
  TCP    127.0.0.1:44000        0.0.0.0:0              LISTENING
  TCP    127.0.0.1:49678        0.0.0.0:0              LISTENING
  TCP    127.0.0.1:50721        0.0.0.0:0              LISTENING
  TCP    127.0.0.1:52600        0.0.0.0:0              LISTENING
  TCP    127.0.0.1:57105        0.0.0.0:0              LISTENING
  TCP    127.0.0.1:60110        0.0.0.0:0              LISTENING
  TCP    127.0.0.1:63417        0.0.0.0:0              LISTENING
  TCP    127.0.0.1:63418        0.0.0.0:0              LISTENING
  TCP    127.0.0.1:63419        0.0.0.0:0              LISTENING
  TCP    172.16.22.66:139       0.0.0.0:0              LISTENING
  TCP    172.17.0.1:139         0.0.0.0:0              LISTENING
  TCP    [::]:135               [::]:0                 LISTENING
  TCP    [::]:445               [::]:0                 LISTENING
  TCP    [::]:3389              [::]:0                 LISTENING
  TCP    [::]:5432              [::]:0                 LISTENING
  TCP    [::]:7680              [::]:0                 LISTENING
  TCP    [::]:49664             [::]:0                 LISTENING
  TCP    [::]:49665             [::]:0                 LISTENING
  TCP    [::]:49666             [::]:0                 LISTENING
  TCP    [::]:49667             [::]:0                 LISTENING
  TCP    [::]:49668             [::]:0                 LISTENING
  TCP    [::]:49669             [::]:0                 LISTENING
  TCP    [::]:49674             [::]:0                 LISTENING
  TCP    [::]:49675             [::]:0                 LISTENING
  TCP    [::1]:30523            [::]:0                 LISTENING
  TCP    [::1]:42050            [::]:0                 LISTENING
  TCP    [::1]:49670            [::]:0                 LISTENING
  TCP    [::1]:50721            [::]:0                 LISTENING
PS C:\Users\Jeevan.Fernandes\Downloads> curl -v google.com
VERBOSE: GET with 0-byte payload
VERBOSE: received -1-byte response of content type text/html; charset=UTF-8

Security Warning: Script Execution Risk
Invoke-WebRequest parses the content of the web page. Script code in the web page might be run when the page is
parsed.
      RECOMMENDED ACTION:
      Use the -UseBasicParsing switch to avoid script code execution.

      Do you want to continue?

[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): n
curl : Operation cancelled due to security concerns. Use -UseBasicParsing parameter for safe HTML parsing without
script execution.
At line:1 char:1
+ curl -v google.com
+ ~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (http://www.google.com/:Uri) [Invoke-WebRequest], InvalidOperationExcepti
   on
    + FullyQualifiedErrorId : WebCmdletIEParsingDeclined,Microsoft.PowerShell.Commands.InvokeWebRequestCommand
