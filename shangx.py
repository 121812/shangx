# 赛博上香
# by Forever121
import os
import time

class incense():

    def __init__(self):
        self.smoke = ','
        self.smoke_lines_offset = 0
        self.smoke_columns_offset = 5
        
        self.incense_pattern = '''
             ╱╱┏╮
          ╱╱╱╱╱┃┃
         ╱╱╱╱╱╱┃┃
         ┛┛┛┛┛┛┃┃
         ╱╱╱╱╱╱┃┃
        ╱╱╱╱╱╱ ┃┃
        ╱╱╱╱╱╱ ┃┃
        ╱╱╱╱╱╱ ┃┃
        ╱╱╱╱╱  ┃┃
        ╱╱╱╱╱  ┃┃
        ╱╱╱╱╱  ┃┃
        ╱╱╱╱╱  ┃┃
        ╱╱╱╱╱╱╱╱
        '''

    def format_incense_pattern(self):
        global columns
        # 定义格式化文本行数
        format_incense_pattern = ''
        # 获取终端行列长度
        columns = os.get_terminal_size().columns
        lines = os.get_terminal_size().lines
        # 取列居中位置
        center_lines = lines // 2 - str.count(self.incense_pattern, '\n') // 2

        # 定义烟
        # 定义烟的列上偏移量
        self.smoke_columns_offset = self.smoke_columns_offset + 1 if self.smoke_columns_offset < 9 else 5
        # * 4 方便展示效果
        smoke_columns = self.smoke_columns_offset * 4
        # 定义烟的行内偏移量， 
        self.smoke_lines_offset = self.smoke_lines_offset + 1 if self.smoke_lines_offset < 4 else 0 

        smoke = ' ' * smoke_columns + self.smoke + '\n' * self.smoke_lines_offset

        center_lines -= self.smoke_lines_offset

        text = '\n' * center_lines + '\n'+ smoke + self.incense_pattern
        # print(lines, center_lines, smoke_columns, self.smoke_lines_offset)

        # 绘制文本图形
        for i in text.split('\n'):
            # 取行居中位置
            center_columns = (columns - len(i)) // 2
            # 拼接
            format_incense_pattern = format_incense_pattern + '\n' + ' ' * center_columns + i 
        print(format_incense_pattern, flush=True)


st = incense()

interval = 0.5
# windows
if os.name == 'nt':
    for i in range(0, 14): 
        os.system('cls')
        st.format_incense_pattern()
        time.sleep(interval)
    exit(0)


# linux
try:
    os.system('tput civis')
    for i in range(0, 14): 
        os.system('clear')
        st.format_incense_pattern()
        # break
        time.sleep(interval)
    os.system('tput cnorm')

except KeyboardInterrupt:
    os.system('tput cnorm')