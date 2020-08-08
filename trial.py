



  
import discord



from discord.ext import commands,tasks



client = commands.Bot(command_prefix=".")

    

@client.command()
async def hello(ctx):
    
    author=ctx.author
    
    if(str(author)=='Blaze777#2388'):
        await ctx.send('Hello Dear Boss ')



    elif(str(author)=='siddharthc30#7363'):
        await ctx.send('Hey Hows Rowdy ')

    
        
    
    else:
        await ctx.send('Hello {}'.format(ctx.author))

@client.command()
async def Add(ctx, arg1, arg2):

    
    
    
    tmessage=await ctx.send('Assignment {}'.format(arg2))
    await tmessage.pin()


@client.command()
async def display(ctx):

    list=await ctx.pins()
    print(list)

    for li in list:
        await ctx.send(li.content)
        
    

    
    



        
        
    
    
    



        
    
    
    


    






client.run('NzQxMzIwNjIwNzA4NDYyNjkz.Xy12oQ.DfVvVvZjBhy-5Lkz48tHXUKVqxU')


