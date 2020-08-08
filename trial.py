



  
import discord



from discord.ext import commands



client = commands.Bot(command_prefix=".")

    

@client.command()
async def hello(ctx):
    
    
    await ctx.send('Hello {}'.format(ctx.author))

@client.command()
async def Add(ctx, arg1, arg2):

    
    
    
    tmessage=await ctx.send('Assignment {}'.format(arg2))
    await tmessage.pin()
    
    


@client.event
async def on_reaction_add(reaction, user):
    cemoji=reaction.emoji
    if(cemoji == "👌"):
        tmessage=reaction.message
        if tmessage.author == client.user:
            await tmessage.channel.send('pinning this message :wink:')
            await tmessage.pin()
            

   
     
            

    else:
        tmessage=reaction.message
        await tmessage.channel.send('I wont do anything k? :unamused:')
        
        
    
    
    


@client.command()
async def display(ctx):

    for dt in data:
        await ctx.send('Assignments Pending: {} '.format(dt))
        
    
    
    


    






client.run('NzQxMzIwNjIwNzA4NDYyNjkz.Xy12oQ.DfVvVvZjBhy-5Lkz48tHXUKVqxU')


