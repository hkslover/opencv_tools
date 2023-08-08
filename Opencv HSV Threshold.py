from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from typing import Dict
import cv2
from PIL import Image, ImageTk
import windnd
import numpy as np
import pyperclip
class WinGUI(Tk):
    widget_dic: Dict[str, Widget] = {}
    def __init__(self):
        super().__init__()
        self.__win()
        self.lower_hue = tk.IntVar()
        self.upper_hue = tk.IntVar()
        self.lower_saturation = tk.IntVar()
        self.upper_saturation = tk.IntVar()
        self.lower_value = tk.IntVar()
        self.upper_value = tk.IntVar()

        self.invert_value = IntVar()
        self.invert_value.set(0)
        self.lower_hue.set(0)
        self.upper_hue.set(180)
        self.lower_saturation.set(0)
        self.upper_saturation.set(255)
        self.lower_value.set(0)
        self.upper_value.set(255)

        self.widget_dic["tk_label_ll1yhppq"] = self.__tk_label_ll1yhppq(self)
        self.widget_dic["tk_label_ll1yhyvq"] = self.__tk_label_ll1yhyvq(self)
        self.widget_dic["tk_scale_ll1yihwp"] = self.__tk_scale_ll1yihwp(self)
        self.widget_dic["tk_scale_ll1yixh7"] = self.__tk_scale_ll1yixh7(self)
        self.widget_dic["tk_scale_ll1yjgkm"] = self.__tk_scale_ll1yjgkm(self)
        self.widget_dic["tk_scale_ll1yjjnv"] = self.__tk_scale_ll1yjjnv(self)
        self.widget_dic["tk_scale_ll1yjlkv"] = self.__tk_scale_ll1yjlkv(self)
        self.widget_dic["tk_scale_ll1yjp8v"] = self.__tk_scale_ll1yjp8v(self)
        self.widget_dic["tk_button_ll1yjxrm"] = self.__tk_button_ll1yjxrm(self)
        self.widget_dic["tk_check_button_ll20wlg6"] = self.__tk_check_button_ll20wlg6(self)
        self.widget_dic["tk_button_ll214e5u"] = self.__tk_button_ll214e5u(self)
    def __win(self):
        self.title("Opencv HSV Threshold")
        # 设置窗口大小、居中
        width = 796
        height = 520
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)
        # 自动隐藏滚动条      
    def scrollbar_autohide(self,bar,widget):
        self.__scrollbar_hide(bar,widget)
        widget.bind("<Enter>", lambda e: self.__scrollbar_show(bar,widget))
        bar.bind("<Enter>", lambda e: self.__scrollbar_show(bar,widget))
        widget.bind("<Leave>", lambda e: self.__scrollbar_hide(bar,widget))
        bar.bind("<Leave>", lambda e: self.__scrollbar_hide(bar,widget))
    
    def __scrollbar_show(self,bar,widget):
        bar.lift(widget)
    def __scrollbar_hide(self,bar,widget):
        bar.lower(widget)
    
    def vbar(self,ele, x, y, w, h, parent):
        sw = 15 # Scrollbar 宽度
        x = x + w - sw
        vbar = Scrollbar(parent)
        ele.configure(yscrollcommand=vbar.set)
        vbar.config(command=ele.yview)
        vbar.place(x=x, y=y, width=sw, height=h)
        self.scrollbar_autohide(vbar,ele)
    def __tk_label_ll1yhppq(self,parent):
        label = Label(parent,text="image",anchor="center", )
        label.place(x=20, y=20, width=359, height=220)
        return label
    def __tk_label_ll1yhyvq(self,parent):
        label = Label(parent,text="mask",anchor="center", )
        label.place(x=420, y=20, width=359, height=220)

        return label
    def __tk_scale_ll1yihwp(self,parent):
        scale = Scale(parent,from_=0, to=180,orient=HORIZONTAL,  variable=self.lower_hue)
        scale.place(x=20, y=250, width=764, height=31)

        return scale
    def __tk_scale_ll1yixh7(self,parent):
        scale = Scale(parent, from_=0, to=180,orient=HORIZONTAL, variable=self.upper_hue)
        scale.place(x=20, y=290, width=764, height=31)

        return scale
    def __tk_scale_ll1yjgkm(self,parent):
        scale = Scale(parent, from_=0, to=255,orient=HORIZONTAL, variable=self.lower_saturation)
        scale.place(x=20, y=330, width=764, height=31)
        return scale
    def __tk_scale_ll1yjjnv(self,parent):
        scale = Scale(parent, from_=0, to=255,orient=HORIZONTAL, variable=self.upper_saturation)
        scale.place(x=20, y=370, width=764, height=31)

        return scale
    def __tk_scale_ll1yjlkv(self,parent):
        scale = Scale(parent, from_=0, to=255,orient=HORIZONTAL, variable=self.lower_value)
        scale.place(x=20, y=410, width=764, height=31)

        return scale
    def __tk_scale_ll1yjp8v(self,parent):
        scale = Scale(parent, from_=0, to=255,orient=HORIZONTAL, variable=self.upper_value)
        scale.place(x=20, y=450, width=764, height=31)
        return scale
    def __tk_button_ll1yjxrm(self,parent):
        btn = Button(parent, text="copy", takefocus=False,)
        btn.place(x=660, y=480, width=120, height=33)
        return btn 
    def __tk_check_button_ll20wlg6(self,parent):
        cb = Checkbutton(parent,text="invert", variable=self.invert_value)
        cb.place(x=553, y=482, width=80, height=33)
        return cb
    def __tk_button_ll214e5u(self,parent):
        btn = Button(parent, text="reset", takefocus=False,)
        btn.place(x=20, y=480, width=120, height=33)
        return btn
class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()
        self.lower_hue_scale = self.widget_dic["tk_scale_ll1yihwp"]
        self.upper_hue_scale = self.widget_dic["tk_scale_ll1yixh7"]
        self.lower_saturation_scale = self.widget_dic["tk_scale_ll1yjgkm"]
        self.upper_saturation_scale = self.widget_dic["tk_scale_ll1yjjnv"]
        self.lower_value_scale = self.widget_dic["tk_scale_ll1yjlkv"]
        self.upper_value_scale = self.widget_dic["tk_scale_ll1yjp8v"]
        
        self._image = None
        self._mask = None
    def hsv_update(self,*args):
        lower_bound = np.array([self.lower_hue.get(), self.lower_saturation.get(), self.lower_value.get()])
        upper_bound = np.array([self.upper_hue.get(), self.upper_saturation.get(), self.upper_value.get()])
        self._mask = cv2.inRange(cv2.cvtColor(self._image, cv2.COLOR_BGR2HSV), lower_bound, upper_bound)
        if self.invert_value.get():
            self._mask = cv2.bitwise_not(self._mask)
        label = self.widget_dic["tk_label_ll1yhyvq"]
        image = ImageTk.PhotoImage(image=Image.fromarray(self._mask))
        label.config(image=image)
        label.img = image
    def on_drop(self,files):
        file_path = '\n'.join((item.decode('gbk') for item in files))
        label = self.widget_dic["tk_label_ll1yhppq"]
        image = cv2.imread(file_path)
        self._image = cv2.resize(image,(359,220))
        image_rgb = cv2.cvtColor(self._image, cv2.COLOR_BGR2RGB)
        image = ImageTk.PhotoImage(image=Image.fromarray(image_rgb))
        label.config(image=image)
        label.img = image
        self.hsv_update()
    def copy_hsv_value(self,event):
        data = '''low = np.array([{0}, {2}, {4}])
upper = np.array([{1}, {3}, {5}])'''.format(self.lower_hue.get(),self.upper_hue.get(),
                   self.lower_saturation.get(),self.upper_saturation.get(), 
                   self.lower_value.get(),self.upper_value.get())
        pyperclip.copy(data)
    def scale_reset(self,event):
        self.lower_hue.set(0)
        self.upper_hue.set(180)
        self.lower_saturation.set(0)
        self.upper_saturation.set(255)
        self.lower_value.set(0)
        self.upper_value.set(255)
    def image_click(self,event):
        x = event.x
        y = event.y
        bgr_color = np.uint8([[self._image[y,x]]])
        hsv_color = cv2.cvtColor(bgr_color, cv2.COLOR_BGR2HSV)[0][0]
        print(hsv_color)
        
    def __event_bind(self):
        windnd.hook_dropfiles(self , func=self.on_drop)

        self.lower_hue.trace_add("write",self.hsv_update)
        self.upper_hue.trace_add("write",self.hsv_update)
        self.lower_saturation.trace_add("write",self.hsv_update)
        self.upper_saturation.trace_add("write",self.hsv_update)
        self.lower_value.trace_add("write",self.hsv_update)
        self.upper_value.trace_add("write",self.hsv_update)
        self.invert_value.trace_add("write",self.hsv_update)
        self.widget_dic["tk_button_ll1yjxrm"].bind('<Button-1>',self.copy_hsv_value)
        self.widget_dic["tk_button_ll214e5u"].bind('<Button-1>',self.scale_reset)

        self.widget_dic["tk_label_ll1yhppq"].bind("<Button-1>", self.image_click)

if __name__ == "__main__":
    win = Win()
    win.mainloop()