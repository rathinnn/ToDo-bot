



  
import discord



from discord.ext import commands

f = open("test.txt",'r')
data=f.read().splitlines()

data = list(filter(None, data))
f.close()

client = commands.Bot(command_prefix="<#>")

@client.command()
async def hello(ctx, arg):
    
    
    await ctx.send('Hello {}'.format(ctx.author))

@client.command()
async def Add(ctx, arg1, arg2):

    
    data.append(str(arg2))
    
    await ctx.send('Adding {} to List Of Assignments'.format(arg2))

@client.command()
async def display(ctx):

    for dt in data:
        await ctx.send('Assignments Pending: {} '.format(dt))
        
    
    
    


    






client.run('NzQxMzIwNjIwNzA4NDYyNjkz.Xy12oQ.DfVvVvZjBhy-5Lkz48tHXUKVqxU')

f = open("test.txt",'w')

for i in range (len(data)):
    if i is not len(data)-1:
        data[i]=data[i]+'\n'
    
f.writelines(data)
f.close()
