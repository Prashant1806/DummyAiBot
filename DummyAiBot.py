import wolframalpha
import time



time.sleep(0.5)
name = input("Please enter your name:")
time.sleep(0.5)
print("HELLO "+name.upper())
time.sleep(0.5)
print("HOW CAN I HELP YOU!")
while 1:

    user = input("Ques>>:")
    id ="K6JPLA-246YUHR3PA"
    me = wolframalpha.Client('K6JPLA-246YUHR3PA')
    try:
        res = me.query(user)
        ans = next(res.results).text
        print ("BOT: " +ans)
    except:
        print("OOPS!! I CANNOT FIND IT!!\n Please try some other stuff!!")
