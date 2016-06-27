'''

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'password'

# creates a cipher helper with each letter substituted
# by the corresponding character in the key
c = VigenereCipher(key, alphabet)

c.encode('codewars'); # returns 'rovwsoiv'
c.decode('laxxhsj'); # returns 'waffles'

# returns 'pmsrebxoy rev lvynmylatcwu dkvzyxi bjbswwaib'
c.encode('amazingly few discotheques provide jukeboxes')

# returns 'amazingly few discotheques provide jukeboxes'
c.decode('pmsrebxoy rev lvynmylatcwu dkvzyxi bjbswwaib')

'''

class VigenereAutokeyCipher:
    def __init__(self, key, abc):
        print "key:",key
        print "abc:",abc
        self.keyOrig = key
        self.key = key
        self.abc = abc

    def encode(self, text):
        self.key = self.keyOrig
        print "encrypt: ",self.key
        return self.modem(text, "encrypt")

    def decode(self, text):
        self.key = self.keyOrig
        print "decrypt: ",self.key
        return self.modem(text, "decrypt")

    def modem(self, message, mode):
        print "Message: ",message
        keyid = 0
        t = []
        for s in message:
            #print "key: ",self.key
            num = self.abc.find(s)
            if num != -1: # In alphabet
                if mode == 'encrypt':
                    num += self.abc.find(self.key[keyid])
                elif mode == 'decrypt':
                    num -= self.abc.find(self.key[keyid])

                num = num%len(self.abc) if num!=-1 else 0

                t.append(self.abc[num])

                keyid += 1 # move to the next letter in the key
                if keyid == len(self.key):
                    self.key = self.keyOrig+''.join(filter(lambda x:x in self.abc, t)) if mode == 'decrypt' else self.keyOrig+''.join(filter(lambda x:x in self.abc, list(message)))

            else:
                print "Excluding: ",s
                t.append(s)
        res = ''.join(t)
        print "Res: ",res
        return res
