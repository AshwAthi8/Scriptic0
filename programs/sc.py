s=arr=[0x00, 0x0c, 0x11, 0x25, 0x30, 0x31, 0x08, 0x61, 0x1d, 0x03, 0x3f, 0x39, 0x2d, 0x27, 0x1a, 0x76, 0x1a, 0x32, 0x41, 0x26, 0x47, 0x2f]
a="REEvurs"
f=""
for i in range(len(s)):
	f=f+chr(ord(a[i%len(a)])^s[i])

	print(f)