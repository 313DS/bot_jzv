from pyrogram import Client, filters
from pyrogram.types import Message,ReplyKeyboardMarkup, KeyboardButton

API_ID = '26910800'
API_HASH = '1bf8eb38fad5c2fae396ee253e1227b8'
BOT_TOKEN = '6358583765:AAEQtwdN66T39aWJMXWydr2t0ItwJzQFEvs'
CHANNEL_USERNAME = '@your_channel_username'

proxy = {
     "scheme": "socks5", 
     "hostname": "127.0.0.1",
     "port": 10808,
 }
# Initialize the Pyrogram Client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN,proxy=proxy,)
print('ok1')


@app.on_message(filters.command("start"))
async def start(client, message: Message):

    keyboard = ReplyKeyboardMarkup(
    [
    [
        KeyboardButton("فیزیولوژی گوارش"),
        KeyboardButton("جزوه ادبیات"),
        KeyboardButton("زبان تخصصی ۱")
    ],
    [
        KeyboardButton("علوم تشریح سروگردن"),
        KeyboardButton("علوم تشریح قلب"),
        KeyboardButton("فیزیولوژی گردش خون")    
    ],
    [
        KeyboardButton("آناتومی گوارش"),
        KeyboardButton("بیوشیمی دیسیپلین"),
        KeyboardButton("فیزیولوژی قلب"),
    ],
    [  
        KeyboardButton("بهمن99-فیزیو گوارش"),
        KeyboardButton("بهمن99-آناتومی قلب"),
        KeyboardButton("بهمن99 فیزیو گردش خون"),
    ],
    [
        KeyboardButton("بهمن 99-آناتومی گوارش"),
        KeyboardButton("بهمن99-فیزیولوژی قلب"),
        KeyboardButton("بهمن99-علوم‌تشریح‌سروگردن"),
    ]
    ],
    
        resize_keyboard=True,
        one_time_keyboard=True
        )

    await message.reply_text(
        text=":جزوه مورد نظر رو انتخاب کتید",
        reply_markup=keyboard
    )
print('ok2')
# Define the message handler
@app.on_message(filters.text)
async def handle_message(client, message: Message):
    text = message.text.lower()
    keyboard = ReplyKeyboardMarkup(
    [
    [
        KeyboardButton("فیزیولوژی گوارش"),
        KeyboardButton("جزوه ادبیات"),
        KeyboardButton("زبان تخصصی ۱")
    ],
    [
        KeyboardButton("علوم تشریح سروگردن"),
        KeyboardButton("علوم تشریح قلب"),
        KeyboardButton("فیزیولوژی گردش خون"),
    ],
    [
        KeyboardButton("آناتومی گوارش"),
        KeyboardButton("بیوشیمی دیسیپلین") ,
        KeyboardButton("فیزیولوژی قلب"), 
    ],
    [
    
        KeyboardButton("بهمن99-فیزیو گوارش"),
        KeyboardButton("بهمن99-آناتومی قلب"),
        KeyboardButton("بهمن99 فیزیو گردش خون"),
    ],
    [
        KeyboardButton("بهمن 99-آناتومی گوارش"),
        KeyboardButton("بهمن99-فیزیولوژی قلب"),
        KeyboardButton("بهمن99-علوم‌تشریح‌سروگردن"),
    ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
    )

    if text == "hello":
        await message.reply("Hi there!")

    elif "بهمن99 فیزیو گردش خون" in text:
        chat_id=message.chat.id
        await client.forward_messages(
    chat_id=chat_id,
    from_chat_id=-1001916847177,
    message_ids=[47]
    )
        

    elif "بهمن99-آناتومی قلب" in text:    
        chat_id=message.chat.id
        await client.forward_messages(
    chat_id=chat_id,
    from_chat_id=-1001916847177,
    message_ids=[48,50,51]
    )
        
    elif "بهمن99-فیزیو گوارش" in text:    
        chat_id=message.chat.id
        await client.forward_messages(
    chat_id=chat_id,
    from_chat_id=-1001916847177,
    message_ids=[46]
    ) 
        
    elif "بهمن 99-آناتومی گوارش" in text:    
        chat_id=message.chat.id
        await client.forward_messages(
    chat_id=chat_id,
    from_chat_id=-1001916847177,
    message_ids=[49]
    )
        
    elif "بهمن99-علوم‌تشریح‌سروگردن" in text:    
        chat_id=message.chat.id
        await client.forward_messages(
    chat_id=chat_id,
    from_chat_id=-1001916847177,
    message_ids=[53,54]
    )
        
    elif "بهمن99-فیزیولوژی قلب"  in text:    
        chat_id=message.chat.id
        await client.forward_messages(
    chat_id=chat_id,
    from_chat_id=-1001916847177,
    message_ids=[52]
    )
        

    elif "فیزیولوژی گردش خون" in text:    
        chat_id=message.chat.id
        await client.forward_messages(
    chat_id=chat_id,
    from_chat_id=-1001916847177,
    message_ids=38
    )
        
    elif "فیزیولوژی گوارش" in text:    
        chat_id=message.chat.id
        await client.forward_messages(
    chat_id=chat_id,
    from_chat_id=-1001916847177,
    message_ids=40
    )
        
    elif "علوم تشریح قلب" in text:      
        chat_id=message.chat.id
        await client.forward_messages(
    chat_id=chat_id,
    from_chat_id=-1001916847177,
    message_ids=[30,31,32]  
    )

    
    elif "علوم تشریح سروگردن" in text:      
        chat_id=message.chat.id
        await client.forward_messages(
    chat_id=chat_id,
    from_chat_id=-1001916847177,
    message_ids=[27,28]
    )

    elif "زبان تخصصی ۱" in text:  
        chat_id=message.chat.id
        await client.forward_messages(
    chat_id=chat_id,
    from_chat_id=-1001916847177,
    message_ids=42
    )

    elif "جزوه ادبیات" in text:  
        chat_id=message.chat.id
        await client.forward_messages(
    chat_id=chat_id,
    from_chat_id=-1001916847177,
    message_ids=20
    )

    elif "بیوشیمی دیسیپلین" in text:    
        chat_id=message.chat.id
        await client.forward_messages(
        chat_id=chat_id,
        from_chat_id=-1001916847177,
        message_ids=[34, 35, 36], 
    )
        
    elif "آناتومی گوارش" in text:    
        chat_id=message.chat.id
        await client.forward_messages(
        chat_id=chat_id,
        from_chat_id=-1001916847177,
        message_ids=[43, 44], 
    )
    elif "فیزیولوژی قلب" in text:    
        chat_id=message.chat.id
        await client.forward_messages(
        chat_id=chat_id,
        from_chat_id=-1001916847177,
        message_ids=[45], 
        )


    else:
        print('error')
        # Handle unknown commands or messages
        pass
print('ok')

if __name__ == "__main__":
    print(" ╰─>  Runing ...")
    app.run()