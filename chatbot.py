import openai

openai.api_key = "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"


messages = []
system_msg = input("what type of chatbox would you like to create?\n")
messages.append({"role":"system","content":system_msg})
print('Ask me About :',system_msg )

print("your new assistant is ready!")
while input != "quit()":
    message = input("User:")
    messages.append({"role":"user","content":message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role":"assistant","content":reply})
    print("\n"+ reply + "\n")
print("your new assistant is ready!")




