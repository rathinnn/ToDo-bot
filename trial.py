import discord
from discord.ext import commands,tasks
from datetime import datetime
import asyncio

tempcode='''from datetime import datetime
message = "biology;assignment 1;21-12-2021;18:14:33"
message.replace(" ", "")
message_array = message.split(";")
subject_of_assignment = message_array[0].strip();
assignment_name = message_array[1].strip()
date_time_string = message_array[2].strip() + " " + message_array[3].strip()
date_time = datetime.strptime(date_time_string, "%d-%m-%Y %H:%M:%S")
print("subject:" + subject_of_assignment)
print("Assignment_name:" + assignment_name)
print(date_time)
biology;assignment 1;21-12-2021;18:14:33
biology;assignment 1;21-12-2021;18:14:33
biology ;assignment 1;21-12-2021;18:14:33'''

client = commands.Bot(command_prefix="!!")
client.remove_command("help")

@client.command()
async def add(ctx, arg1):
    message=arg1
    message.replace(" ", "")
    message_array = message.split(";")
    if(len(message_array) != 4):
        await ctx.send('Invalid Format')
        return
    subject_of_assignment = message_array[0].strip()
    assignment_name = message_array[1].strip()
    date_time_string = message_array[2].strip() + " " + message_array[3].strip()
    try:
        date_time = datetime.strptime(date_time_string, "%d-%m-%Y %H:%M:%S")
        tmessage=await ctx.send('{}   {}   {}'.format(subject_of_assignment,assignment_name,date_time_string))
        await tmessage.pin()
    except:
        await ctx.send('Invalid Format ')

@client.command()
async def display(ctx):
    list=await ctx.pins()
    for li in list:
        await ctx.send(li.content)

@client.command()
async def checktime(ctx):
    list2=await ctx.pins()
    await ctx.send('Assignments with Deadlines approaching')
    for li in list2:
        message=li.content
        message_array = message.split()
        subject_of_assignment = message_array[0].strip();
        assignment_name = message_array[1].strip()
        date_time_string = message_array[2].strip() + " " + message_array[3].strip()
        date_time = datetime.strptime(date_time_string, "%d-%m-%Y %H:%M:%S")
        now=datetime.now()
        difference=date_time-now
        difference=difference.days
        if(date_time<=now):
            await li.unpin()
        elif(difference<=2 ):
            await ctx.send(li.content+' :  in '+str(difference)+'  days')

@client.command()
async def delete(ctx):
    i=1
    cmessage=ctx.message
    list=await ctx.pins()
    await ctx.send('Choose Assingment to Delete')
    for li in list:
        await ctx.send(str(i)+': '+li.content)
        i=i+1
    def check2(m):
        return m.author == cmessage.author
    try:
        msg = await client.wait_for('message', check=check2, timeout=30.0)
    except asyncio.TimeoutError:
        return await ctx.send('Sorry, you took too long')
    try:
        todel=msg.content
        todel=int(todel)
        li=list[todel-1]
        await li.unpin()
        await ctx.send('deleted '+li.content)
    except:
        await ctx.send('Something went Wrong')

@client.command()
async def modify(ctx):
    i=1
    cmessage=ctx.message
    list=await ctx.pins()
    await ctx.send('Choose Assingment to Modify')
    for li in list:
        await ctx.send(str(i)+': '+li.content)
        i=i+1
    def check3(m):
        return m.author == cmessage.author
    try:
        msg = await client.wait_for('message', check=check3, timeout=30.0)
    except asyncio.TimeoutError:
        return await ctx.send('Sorry, you took too long')
    try:
        todel=msg.content
        todel=int(todel)
        li=list[todel-1]
    except:
        return await ctx.send('Something went Wrong')
    toedit=li.content
    message_array = toedit.split()
    subject_of_assignment = message_array[0].strip();
    assignment_name = message_array[1].strip()
    await ctx.send('Enter New Time')
    try:
        msg = await client.wait_for('message', check=check3, timeout=30.0)
    except asyncio.TimeoutError:
        return await ctx.send('Sorry, you took too long')
    toput=msg.content
    message_array = toput.split(";")
    try:
        date_time_string = message_array[0].strip() + " " + message_array[1].strip()
        date_time = datetime.strptime(date_time_string, "%d-%m-%Y %H:%M:%S")
        tmessage=await ctx.send('{}   {}   {}'.format(subject_of_assignment,assignment_name,date_time_string))
        await tmessage.pin()
    except:
        return await ctx.send('Invalid Format')

@client.command()
async def help(ctx):
    await ctx.send('"!!help" - prints the list of commands for the bot')
    await ctx.send('"!!add [subject];[assignment or exam and its number];[dd-mm-yyyy];[hh:mm:ss in 24 houurs clock format]" - use this format in order to add a entry to the assignment list')
    await ctx.send('"!!delete" - used to delete a entry in the assignment list and also the next command would be to choose the number of the entry to delete and you need to just enter the number of the entry to delete')
    await ctx.send('"!!modify" - used to modify the time of a particular entry and also the next command would be to choose the number of the entry to modify and you need to just enter the date and time in the following format [dd-mm-yy;hh:mm:ss]')
    await ctx.send('"!!checktime" - prints the list of assignments which are to be submitted in two days in the list')
    await ctx.send('"!!display" - prints all the entries of assignments in the list')

client.run('NzQxMzIwNjIwNzA4NDYyNjkz.Xy12oQ.DfVvVvZjBhy-5Lkz48tHXUKVqxU')
