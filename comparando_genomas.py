
#%%
def createGenomeStruct():
  cont = {}

  for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
      cont[i + j] = 0
  
  return cont

def calculateGenomeFile(file):

  struct = createGenomeStruct()
  
  entrada = file.replace('\n', '')

  for k in range(len(entrada)-1):
    struct[entrada[k] + entrada[k+1]] += 1

  return struct

def generateHtml(outPutFile, struct):
  i = 1
  for k in struct:
    transparencia = struct[k]/max(struct.values())
    outPutFile.write("<div style='color: #fff; width:100px; border: 1px solid #111; height: 100px; float: left; background-color:rgba(0, 0, 0, "+ str(transparencia) +")'>"+ k +"</div>")
    if i%4 == 0:
      outPutFile.write("<div style='clear:both'></div>")
    i += 1

  outPutFile.close()

entradaBacteria = open('arqs/bacteria.fasta').read()
saidaBacteria = open('arqs/bacteria.html', 'w')

estrutura = calculateGenomeFile(entradaBacteria)
generateHtml(saidaBacteria, estrutura)

entradaHuman = open('arqs/human.fasta').read()
saidaHuman = open('arqs/human.html', 'w')

estrutura = calculateGenomeFile(entradaHuman)
generateHtml(saidaHuman, estrutura)

# -----------

# entrada = open('arqs/bacteria.fasta').read()
# saida = open('arqs/bacteria.html', 'w')

# cont = {}

# for i in ['A', 'T', 'C', 'G']:
#   for j in ['A', 'T', 'C', 'G']:
#     cont[i + j] = 0

# entrada = entrada.replace('\n', '')

# for k in range(len(entrada)-1):
#   cont[entrada[k] + entrada[k+1]] += 1

# HTML

i = 1

# for k in cont:
#   transparencia = cont[k]/max(cont.values)
#   saida.write("<div style='color: #fff; width:100px; border: 1px solid #111; height: 100px; float: left; background-color:rgba(0, 0, 0, "+ str(transparencia) +")'>"+ k +"</div>")
#   if i%4 == 0:
#     saida.write("<div style='clear:both'></div>")
#   i += 1

# saida.close()