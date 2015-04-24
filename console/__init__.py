class message:
    blk    ='\033[0;30m' # Black - Regular
    red    ='\033[0;31m' # Red
    grn    ='\033[0;32m' # Green
    ylw    ='\033[0;33m' # Yellow
    blu    ='\033[0;34m' # Blue
    pur    ='\033[0;35m' # Purple
    cyn    ='\033[0;36m' # Cyan
    wht    ='\033[0;37m' # White
    b_blk  ='\033[1;30m' # Black - Bold
    b_red  ='\033[1;31m' # Red
    b_grn  ='\033[1;32m' # Green
    b_ylw  ='\033[1;33m' # Yellow
    b_blu  ='\033[1;34m' # Blue
    b_pur  ='\033[1;35m' # Purple
    b_cyn  ='\033[1;36m' # Cyan
    b_whi  ='\033[1;37m' # White
    u_blk  ='\033[4;30m' # Black - Underline
    u_red  ='\033[4;31m' # Red
    u_grn  ='\033[4;32m' # Green
    u_ylw  ='\033[4;33m' # Yellow
    u_blu  ='\033[4;34m' # Blue
    u_pur  ='\033[4;35m' # Purple
    u_cyn  ='\033[4;36m' # Cyan
    u_wht  ='\033[4;37m' # White
    bg_blk ='\033[40m'   # Black - Background
    bg_red ='\033[41m'   # Red
    bg_grn ='\033[42m'   # Green
    bg_ylw ='\033[43m'   # Yellow
    bg_blu ='\033[44m'   # Blue
    bg_pur ='\033[45m'   # Purple
    bg_cyn ='\033[46m'   # Cyan
    bg_wht ='\033[47m'   # White
    # High Intensity backgrounds
    bg_Iblk = '\033[0;100m'   # Black
    bg_Ired = '\033[0;101m'   # Red
    bg_Igrn = '\033[0;102m'   # Green
    bg_Iylw = '\033[0;103m'   # Yellow
    bg_Iblu = '\033[0;104m'   # Blue
    bg_Ipur = '\033[0;105m'   # Purple
    bg_Icyn = '\033[0;106m'   # Cyan
    bg_Iwht = '\033[0;107m'   # White
    # High Intensity
    Iblk='\033[0;90m'       # Black
    Ired='\033[0;91m'       # Red
    Igrn='\033[0;92m'       # Green
    Iylw='\033[0;93m'       # Yellow
    Iblu='\033[0;94m'       # Blue
    Ipur='\033[0;95m'       # Purple
    Icyn='\033[0;96m'       # Cyan
    Iwht='\033[0;97m'       # White
    # Bold High Intensity
    b_Iblk ='\033[1;90m'      # Black
    b_Ired ='\033[1;91m'      # Red
    b_Igrn ='\033[1;92m'      # Green
    b_Iylw ='\033[1;93m'      # Yellow
    b_Iblu ='\033[1;94m'      # Blue
    b_Ipur ='\033[1;95m'      # Purple
    b_Icyn ='\033[1;96m'      # Cyan
    b_Iwht ='\033[1;97m'      # White
    #RESET
    RST     = '\033[0m'    # Text Reset
    #Defined
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN= '\033[92m'
    WHITE  = '\033[1m'
    YELLOW = '\033[1;33m'
    WARNING= '\033[93m'
    FAIL   = '\033[91m'

    @classmethod
    def print_err(cls, msg):
        print cls.b_red + msg + cls.RST

    @classmethod
    def print_title(cls, msg):
        print cls.bg_wht + cls.b_blk + msg + cls.RST

    @classmethod
    def print_debug(cls, msg):
        print cls.Iblk + "DEBUG: " + str(msg) + cls.RST

    @classmethod
    def print_step(cls, msg):
        print cls.b_blu + msg + cls.RST

    @classmethod
    def print_value(cls, msg, value):
        print cls.b_Igrn + msg + ': ' + cls.grn + value + cls.RST