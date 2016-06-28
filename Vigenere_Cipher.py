'''

var alphabet = 'abcdefghijklmnopqrstuvwxyz';
var key = 'password';

// creates a cipher helper with each letter substituted
// by the corresponding character in the key
var c = new VigenèreCipher(key, alphabet);

c.encode('codewars'); // returns 'rovwsoiv'
c.decode('laxxhsj'); // returns 'waffles'

'''

class VigenereCipher (object):
    def __init__(self, key, abc):
        print "key:",key
        print "abc:",abc
        self.keyOrig = key.decode("utf-8")
        self.key = key.decode("utf-8")
        self.abc = abc.decode("utf-8")

    def encode(self, text):
        text = text.decode("utf-8")
        self.key = self.keyOrig
        print "encrypt: ",self.key.encode('utf-8')
        return self.modem(text, "encrypt")

    def decode(self, text):
        text = text.decode("utf-8")
        self.key = self.keyOrig
        print "decrypt: ",self.key.encode('utf-8')
        return self.modem(text, "decrypt")

    def modem(self, message, mode):
        print "Message: ",message.encode('utf-8')
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

            else:
                print "Excluding: ",s.encode('utf-8')
                t.append(s)

            keyid += 1 # move to the next letter in the key
            if keyid == len(self.key):
                keyid = 0

        res = ''.join(t)
        print "Res: ",res.encode('utf-8')
        return res.encode('utf-8')
