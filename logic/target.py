class Target():
    __slots__ = ("target_hwnd","cps","window_title","clicker_pos")
    def __init__(self,target_hwnd:int = 0, cps: int = 1,window_title:str = "",clicker_pos:tuple[int,int]= (0,0))-> None:
        self.target_hwnd = target_hwnd
        self.cps = cps
        self.window_title = window_title
        self.clicker_pos = clicker_pos
    def change_cps(self,new_cps:int)-> None:
        self.cps = new_cps
    def change_target(self,new_target:int)-> None:
        self.target_hwnd = new_target
    def change_window_title(self,new_title:str)->None:
        self.window_title = new_title
    def change_clicker_pos(self,new_clicker_pos:tuple[int,int])->None:
        self.clicker_pos = new_clicker_pos
    def has_target(self)-> bool:
        return self.target_hwnd != 0
clicker_target = Target() 
        