# pyflashstm
A python script used to flash some binary into a STM32 microcontroller.

## How to use it ?

First download a copy of OpenOCD[https://openocd.org/],then add the directory `./bin` to path.Run the script as the help content described so the binary could be flashed into the chip.For example.

`python pyflashstm.py stm32g0 .\test.bin`

A return code will be displayed once the `openocd.exe` stop running.

## So why don't use pyocd?

I dont have a Nucleo Board which is too expensive in China,and THE BEST WAY to flash a binary without Keil MDK is using OpenOCD.The syntax of OpenOCD is simple but I had to input the content again which is simply a terrible experience.

## Will you add other chip into this tool?

I'm planning to add some chips like `STM32H750` because I've bought it last week.But I wouldn't add other chips this time.