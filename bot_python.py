import subprocess
import discord
import asyncio
import os
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.utils import get

#defina aqui o prefixo do bot
prefix = "!"
client = commands.Bot(command_prefix=prefix)
@client.event
async def on_message(message):
    if message.content.startswith(f'{prefix}python'):
        codigo = str(message.content).replace(f'{prefix}python','')
        if("```py" in codigo) == False:
            arq = open('ajuda.txt', 'w')
            arq.write("{prefix}python\n```py\ncodigo\n```")
            arq.close()
            await message.channel.send(file=discord.File(r''+os.getcwd()+'\\ajuda.txt'))
            return;
        if("input" in codigo) == True:
            await message.channel.send("opções de entrada não estão disponiveis")
            return;
        if("```py" in codigo) == True:
                codigo = codigo.replace("```py","")
                codigo = codigo.replace("```","")
                arq = open("arquivo.py", 'w')
                arq.write(codigo)
                arq.close()
                os.system(f'cd  {os.getcwd()}')
                os.system('arquivo.py' + ' > output.txt')
                arq = open('output.txt', 'r')
                output = arq.read()
                arq.close()
                
                try:
                    await message.channel.send(f'```{output}```')
                except:
                    proc = subprocess.Popen("arquivo.py", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    proc = str(proc.stdout.read())
                    proc = ''.join([proc[i] for i in range(len(proc)) if i != 0])
                    proc = ''.join([proc[i] for i in range(len(proc)) if i != 0])
                    if ('C:' in proc) == True:
                        a = int(proc.find("C:"))
                        b = int(proc.find(".py"))
                        print(a,b)
                        proc = proc[:a] +  proc[b:] 
                    
                    arq = open('erros.py', 'w')
                    arq.write(f"variavel = str('{proc})\nprint(variavel)")
                    arq.close()
                    os.system('erros.py' + ' > output_erros.txt')
                    arq = open('output_erros.txt', 'r')
                    output = arq.read()
                    arq.close()
                    await message.channel.send(output)

# coloque o token do seu bot aqui
client.run("token")
