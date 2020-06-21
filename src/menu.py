#by SysFailureError
#date: 06/2020

import sys, os
from inforfile import ext_file
from ytdl_download import YtLogger
from ytdl_download import Download
from base import FileYTVideo, Print, Icons
from base import get_ext, d_exit

_ext = get_ext()
file_obj = FileYTVideo(YtLogger)
ytdl_obj = Download()
pprint_infor = Print()
icon = Icons()

mn = "menu"
md = "media"
sl = "selection"
ad = "audio"
vd = "video"
fmt = "format"

class Menu(object):
    def __init__(self):
        self.getinfor = {
                    "midia"           : None,
                    "format"          : None,
                    "url"             : None,
                    "qualid"          : None, 
                    "new_namefile"    : None, 
        }

menu = Menu()

def show_infor_down():
    pprint_infor.pprint("Midia..: {:5}".format(menu.getinfor[md]))
    pprint_infor.pprint("Formato: {:5}".format(menu.getinfor[fmt]))

def geturl(f):
    os.system("clear")
    msg1 = "[0] {0} {1}".format("Menu Inicial", icon.mn_page2)
    pprint_infor.pprint(msg1)

    pprint_infor.pprint(f"Informe a url do {f}")
    u = str(pprint_infor.pprint(icon.mn_search + " ", func=input, p_normal=False))

    d_volte(u, init_infor_base)

    return u

def get_media():
    pprint_infor.pprint("{0}Escolha o tipo de midia {0}".format(icon.md_ico))
    m0 = "[1] {0:6} {1}".format(ad, icon.md_ad0)
    m1 = "[2] {0:6} {1}".format(vd, icon.md_vd0)
    m2 = "[0] {0:6} {1}".format("Sair", icon.mn_selec6)
    pprint_infor.pprint([m0, m1, m2], p_normal=False)

    a = int(pprint_infor.pprint(f"{icon.mn_selec1} ", func=input, p_normal=False))

    return a

def get_format_media():
    a = get_media()

    if a == 1:
        f = ad
    elif a == 2:
        f = vd
    else:
        f = 0

    d_exit(f)

    pprint_infor.pprint(f"Escolha um dos formatos de {f}")

    c = 1
    for f_media in ext_file[f]:
        msg = "[{0}] {1:6} {2}".format(c, f_media, icon.i_icons[md][1][f][0])
        pprint_infor.pprint(msg)
        c += 1
    msg1 = "[0] {0} {1}".format("Voltar", icon.mn_page1)
    pprint_infor.pprint(msg1)

    b = int(pprint_infor.pprint(f"{icon.mn_selec1} ", func=input, p_normal=False))
    d_volte(b, get_format_media)

    return a, b, f

def d_volte(check_value, volt_func):
    """
    Somente valores do tipo inteiro
    """
    if type(check_value) == int or check_value.isdigit():
        if int(check_value) == 0:
            os.system("clear")
            volt_func()
        else:
            pass
    else:
        pass

def init_infor_base():
    os.system("clear")
    a, b, f = get_format_media()
    u = geturl(f)    

    menu.getinfor[fmt] = ext_file[f][b-1] #b-1 pq mudei os indices das opções
    menu.getinfor[md] = f
    menu.getinfor["url"] = u

    return True


def transfer_information():
    file_obj.infor_video[md] = menu.getinfor[md]
    file_obj.infor_video[fmt] = menu.getinfor[fmt]
    file_obj.infor_video["url"] = menu.getinfor["url"]

    return True
    

def main():
    init_infor_base()
    transfer_information()

    show_infor_down()

    file_obj.init_ytdl_opts()

    ytdl_obj.ytdl_opts = file_obj.ytdl_opts
    ytdl_obj.init_ytdl()
    ytdl_obj.url = file_obj.infor_video["url"]

    ytdl_obj.start()


if __name__ == "__main__":
    main()
