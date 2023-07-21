# ChatPal - Texting Made Secure 
A Encryption and decryption program written in Python . It is capable of switching among random encryption logics to produce a cipher text. This makes it challenging to decipher.
. 

# Screenshots
<img width="545" alt="encrypt" src="https://github.com/aadhar-jain/ChatPal/assets/128128944/5976835d-3ba3-45f7-bbb9-c15308f14a5a">
<img width="548" alt="decrypt" src="https://github.com/aadhar-jain/ChatPal/assets/128128944/c6ca1250-de73-4403-b193-80b6dbbf00b2">

## How to try ?

Just download the zip file , extract it and run **"encrypt.py"** file.

*PYTHON MUST BE INSTALLED ON YOUR SYSTEM, AND A SUPPORTING IDE IS ALSO REQUIRED TO BE INSTALLED. I PERSONALLY PREFER **PYCHARM***

Link to download PyCharm : https://www.jetbrains.com/pycharm/download

**Community edition is available for free**
## User Guide
1. After installing PyCharm (or any IDE) , right click on *'encrypt.py'* and open with PyCharm (your IDE).
2. Run the program , and it will ask for a password to access.
3. Enter -> **permitE** (case sensitive)
4. Start typing your message. You may hit *ENTER* for changing line.
5. After complete message is typed , come to new line and type **"quit"**
6. Your Encrypted text will be generated. After successful generation, copy that encryption.
7. Open *"decrypt.py"* using same steps as done for *"encrypt.py"*
8. Run the program, and it will ask for a password to access.
9. Enter -> **permitD** (case sensitive)
10. Paste the copied encryption in "decryptor"
11. Your encryption will be decrypted & you will be able to read original message.
## Features

- **Multiple random encryption logics, for the same text make it really challenging**
- Use of typewriter effect to encrypt really takes away breath
- Requirement of password to access the encryptor/decryptor adds additional layer of security.
- can encrypt upto 100 lines of text , in a single go.
- User can change line anytime, while inputting the text to be encrypted.
- **Formatting of the input is retained, as it is, during whole process, right from entering text till decoding it.**
- Use of unfamiliar characters in encryption, pose a challenge to anyone trying to decipher real meaning
- Easy to use

## Scope of Improvement
- Use of hash table (dictionary), can be considerably beneficial.  It will not only get the code shorter and precise, but more readable also.
- Exceptional constant time, O(1) taken by hash table to perform search operations, will considerably reduce the overheads in processing.
- The implementation of additional encryption logics will significantly enhance the resilience of the encrypted text against unauthorized decryption attempts.
- **An additional feature which involves soliciting users to create a personalized password prior to encryption. By utilizing this password, we can generate a dynamic encryption logic during runtime. Consequently, only individuals possessing knowledge of the password will have the capability to decrypt the encrypted data. This mirrors the concept of a unique private encryption key, which can be shared exclusively with the intended recipient to facilitate the secure transmission of confidential information.**
## Inspiration

*They say necessity is the mother of invention, and it was true in my case*

It was time when I had just got my new personal device, and I was excited! But my sister had this habit of snooping into my chats. Oh no, the invasion of privacy! 😱

Well, I couldn't let that happen, could I? So, the genius in me sparked to life, and I concocted a devious plan to chat away in secret! I created ChatPal. My sister wouldn't have a single clue about what I was up to.

Mission accomplished! 😎
