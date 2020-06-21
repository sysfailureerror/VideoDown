#by SysFailureError
#date: 06/2020

import os, sys
import json
import copy
import functools
from _decorators import *
from inforfile import ext_file


# path
p_src = os.path.dirname(os.path.abspath(__file__))
modulo_dir = p_src.replace('src', '')
p_rec = os.path.join(modulo_dir, "rec")
f_json = os.path.join(p_rec, "icon.json")



class YTvideo(object):
    def __init__(self):
        self.init_infor_video = {
                            "name"          : None,
                            "canal"         : None,
                            "qualit"        : ["bestvideo/best", "bestaudio/best"],
                            "quant_views"   : 0,
                            "quant_comments": 0,
                            "upload_date"   : "",
                            "url"           : ""
        }

        self.infor_video = copy.deepcopy(self.init_infor_video)


class FileYTVideo(YTvideo):
    def __init__(self, logger, **kwargs):
        super().__init__(**kwargs)
        self.geturltxt = False
        self.add_metad = None
        self.logger = logger
        self.ytdl_opts = {}
        self.infor_video["media"] = None
        self.infor_video["format"] = None
    
    def my_hook(self, d):
        if d['status'] == 'finished':
            print(f'Download concluido, convertento para {self.infor_video["format"]}...')
    
    def postprocessors(self):
        opt = {}
        md = self.infor_video["media"]
        if md == "audio":
            opt["key"] = "FFmpegExtractAudio"
            _prefer = "preferredcodec"
            opt["preferredquality"] = "192"
        else:
            opt["key"] = "FFmpegVideoConvertor"
            _prefer = "preferedformat"
        
        for f in ext_file[md]:
            if self.infor_video["format"] == f:
                opt[_prefer] = f
                    
        postprocessors = [opt]

        return postprocessors
    
    def init_ytdl_opts(self):
        if self.infor_video["media"] == "video":
            self.ytdl_opts["format"] = self.infor_video["qualit"][0]
        else:
            self.ytdl_opts["format"] = self.infor_video["qualit"][1]

        self.ytdl_opts["postprocessors"] = self.postprocessors()

        self.ytdl_opts["logger"] = self.logger()
        self.ytdl_opts["progress_hooks"] = [self.my_hook]


class Print(object):

    """
    Print
    ===========
    
    Feito a partir de `decorators` para modificar os texto em qualquer função que faça impressão.\n
    A implementação ainda está inclompleta. Mas por enquanto está servindo.\n
    + `p_infor` : texto que vai ser imprimido na tela. Se `p_infor` for uma lista ou tupla, vai imprimir 
    os elementos em linhas diferentes. Por exemplo:
        >>> var1 = "variavel 1"
        >>> var2 = "variavel 2"
        >>> pprint_info(var1, var2, p_normal=False)
        variavel 1
        variavel 2
    + `p_normal`: imprimir na tela normalmente, a própria função `print()`.
    + `exit_msg` : função `sys.exit()`. (falta melhorar)
    + `func` : tem o objetivo de ler o texto que serião impresso por outra fuções (na verdade ela somente a pega 
    o valor do antes da função original). (falta implementar suporte a outras funções, por enquanto tem suporte somente
    para a função buildin `input()`, talvez `sys.exit()` também). 
    Ex:
        >>> num = int(pprint_info("Digite um numero: ", func=input))
        Digite um numero: 2020
        >>> num
        >>> 2020
    """

    def __init__(self):

        self.p_infor    = ""
        self.p_normal   = False
        self.func       = None
        self.exit_msg   = ""
    
    def reset_infors(self):
        Print().__init__()
        
    def normal_print(self):
        print(self.p_infor)
    
    def pprint(self, p_infor = [], p_normal=True,
               exit_msg=False, func=None):

        self.p_infor    = p_infor
        self.p_normal   = p_normal
        self.func       = func
        self.exit_msg   = exit_msg

        value = self.init_funcs()
        return value

    def init_funcs(self):
        
        if self.p_normal:
            self.normal_print()
            return True
        
        elif type(self.p_infor) == list or tuple and self.p_normal:
            self.multi_print(self.p_infor)
            return True
        
        else:
            
            if self.func is not None:
                if isinstance(self.func, type(input)):
                    value = self.getorprint_func(self.p_infor)
                    return value

            elif self.exit_msg:
                self.sys_exit(self.p_infor)
                return True
        

    @d_pshow("generator")
    @d_pinfor
    def multi_print(self, p_infor):
        return p_infor          

    def sys_exit(self, p_infor):
        @d_exit_msg
        def foo_print(p_infor):
            return p_infor
    
    def getorprint_func(self, p_infor):
        @d_input
        def foo_print(p_infor):
            return self.p_infor
        return foo_print(self.p_infor)


class Icons(object):
    def __init__(self):
        self.i_icons = self.get_json()

        self.md_ico = self.i_icons["media"][0]
        self.md_ad0 = self.i_icons["media"][1]["audio"][0]
        self.md_ad1 = self.i_icons["media"][1]["audio"][1]
        self.md_vd0 = self.i_icons["media"][1]["video"][0]

        self.mn_page0  = self.i_icons["menu"]["page"][0]
        self.mn_page1  = self.i_icons["menu"]["page"][1]
        self.mn_page2  = self.i_icons["menu"]["page"][2]
        self.mn_search = self.i_icons["menu"]["search"]
        self.mn_file0  = self.i_icons["menu"]["file"][0]
        self.mn_file1  = self.i_icons["menu"]["file"][1]
        self.mn_file1  = self.i_icons["menu"]["file"][2]
        self.mn_selec0 = self.i_icons["menu"]["selection"][0]
        self.mn_selec1 = self.i_icons["menu"]["selection"][1]
        self.mn_selec2 = self.i_icons["menu"]["selection"][2]
        self.mn_selec3 = self.i_icons["menu"]["selection"][3]
        self.mn_selec4 = self.i_icons["menu"]["selection"][4]
        self.mn_selec5 = self.i_icons["menu"]["selection"][5]
        self.mn_selec6 = self.i_icons["menu"]["selection"][6]

        self.result0 = self.i_icons["result"][0]
        self.result1 = self.i_icons["result"][1]
        self.result2 = self.i_icons["result"][2]
        self.result3 = self.i_icons["result"][3]
        self.result4 = self.i_icons["result"][4]

        self.user_opt0 = self.i_icons["user_options"][0]
        self.user_opt1 = self.i_icons["user_options"][1]

        self.react0 = self.i_icons["reactions"][0]
        self.react1 = self.i_icons["reactions"][1]
        self.react2 = self.i_icons["reactions"][2]
        self.react3 = self.i_icons["reactions"][3]
    
    def get_json(self):
        with open(f_json, "r+") as f:
            j = json.load(f)

        return j


def get_ext():
    _ext = []
    for i in list(ext_file.items()):
        _ext += i[1]
    return _ext

def checkout(value, instance):
    pass

def d_exit(value):
    if value == 0:
        sys.exit("Até nunca mais. SaInDo..")
    else:
        os.system("clear")
        return False