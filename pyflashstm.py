import os,sys

OPENOCD_PATH = 'D:\\Programs\\OpenOCD\\'

HELP_CONTENT = \
'''pyflashstm v0.1
A Simple tool to flash STM32 chips with OpenOCD.
Usage:
%s [chip type] [file path]
Chip type can be:
  stm32f1 stm32f4 stm32g0
'''%sys.argv[0]

DEBUGGER_CFG = 'share/openocd/scripts/interface/cmsis-dap.cfg'

START_ADDRESS = '0x08000000' #For STM32 microcontroller the Flash is started in there.

CHIP_TYPE={
    'stm32f1':'share/openocd/scripts/target/stm32f1x.cfg',
    'stm32f4':'share/openocd/scripts/target/stm32f4x.cfg',
    'stm32g0':'share/openocd/scripts/target/stm32g0x.cfg',
}

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(HELP_CONTENT)
        sys.exit(0)
    filename = str(sys.argv[2])
    print('File name is %s'%filename)
    if not sys.argv[1] in CHIP_TYPE:
        print("Chip type not found!")
        sys.exit(0)
    else:
        chip_t = CHIP_TYPE[sys.argv[1]]
    print('Flashing target %s.'%chip_t)
    ret_code=os.system('openocd -f %s -f %s -c "program %s 0x08000000 verify reset exit"'%(os.path.join(OPENOCD_PATH,DEBUGGER_CFG),os.path.join(OPENOCD_PATH,chip_t),os.path.join('./',filename.replace('\\','/'))))
    if ret_code != 0:
        print('Command failed with code %s.'%ret_code)
    else:
        print('Flash success.')