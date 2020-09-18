import pynlpir  # 引入依赖包
pynlpir.open()  # 打开分词器
from ctypes import c_char_p 



pynlpir.nlpir.ImportUserDict(b"userdict.txt")



# path = "电子训练语料.txt"
paths = ["汽车训练语料.txt","电子训练语料.txt"]


for path in paths:
	file = open(path,"r",encoding="utf-8")
	writer = open(path[0:path.index(".")]+"_seg.txt","w",encoding="utf-8")
	lines = file.readlines()

	for line in lines:
		index = line.index(">")
		sentence=line[index+1:line.index("</")]
		segments = pynlpir.segment(sentence, pos_names=None)
		sline = ""
		
		print(segments)
		for segment in segments:
			if(segment[1]==None):
				continue
			sline = sline+  "/".join(segment)+ " "
		print(sline)
		writer.write(sline+"\n")

	file.close()
	writer.close
